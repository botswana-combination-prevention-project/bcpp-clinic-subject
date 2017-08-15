from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django_crypto_fields.fields.firstname_field import FirstnameField

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO_UNKNOWN, GENDER_UNDETERMINED, YES_NO_NA, YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import UniqueSubjectIdentifierModelMixin
from edc_map.model_mixins import MapperDataModelMixin
from edc_map.site_mappers import site_mappers
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugModelMixin

from ..choices import VERBAL_HIVRESULT_CHOICE, INABILITY_TO_PARTICIPATE_REASON
from ..eligibility import Eligibility
from ..screening_identifier import ScreeningIdentifier


class EligibilityManager(models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(
            screening_identifier=screening_identifier
        )


class SubjectEligibility (UniqueSubjectIdentifierModelMixin, SearchSlugModelMixin,
                          UpdatesOrCreatesRegistrationModelMixin, MapperDataModelMixin,
                          BaseUuidModel):
    """A model completed by the user that confirms and saves eligibility
    information for potential participant.
    """

    screening_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report date',
        default=get_utcnow,
        validators=[datetime_not_future])

    first_name = FirstnameField(
        verbose_name='First name',
        validators=[RegexValidator("^[A-Z]{1,250}$", "Ensure first name is in CAPS and "
                                   "does not contain any spaces or numbers")],
        help_text="")

    initials = models.CharField(
        verbose_name='Initials',
        max_length=3,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(3),
            RegexValidator("^[A-Z]{1,3}$", "Must be Only CAPS and 2 or 3 letters. No spaces or numbers allowed.")],
        help_text="")

    age_in_years = models.IntegerField(
        verbose_name='Age in years as reported by patient')

    guardian = models.CharField(
        verbose_name="If minor, is there a guardian available? ",
        max_length=10,
        choices=YES_NO_NA,
        help_text="If a minor age 16 and 17, ensure a guardian is available otherwise"
                  " participant will not be enrolled.")

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER_UNDETERMINED)

    has_identity = models.CharField(
        verbose_name="[Interviewer] Has the subject presented a valid OMANG or other identity document?",
        max_length=10,
        choices=YES_NO,
        help_text='Allow Omang, Passport number, driver\'s license number or Omang receipt number. '
                  'If \'NO\' participant will not be enrolled.')

    citizen = models.CharField(
        verbose_name="Are you a Botswana citizen? ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        help_text="")

    legal_marriage = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana Citizen?",
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If 'NO' participant is not eligible.")

    marriage_certificate = models.CharField(
        verbose_name=(
            "[Interviewer] Has the participant produced the marriage certificate, as proof? "),
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If 'NO' participant is not eligible.")

    part_time_resident = models.CharField(
        verbose_name="In the past 12 months, have you typically spent 3 or"
                     " more nights per month in this community? ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        help_text=(
            "If participant has moved into the "
            "community in the past 12 months, then "
            "since moving in has the participant typically "
            "spent more than 3 nights per month in this community. "
            "If 'NO (or don't want to answer)' STOP. Participant is not eligible."),
    )

    literacy = models.CharField(
        verbose_name="Is the participant LITERATE?, or if ILLITERATE, is there a"
                     "  LITERATE witness available ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        help_text="If participate is illiterate, confirm there is a literate"
                  "witness available otherwise participant is not eligible.")

    inability_to_participate = models.CharField(
        verbose_name="Do any of the following reasons apply to the participant?",
        max_length=17,
        choices=INABILITY_TO_PARTICIPATE_REASON,
        help_text=("Participant can only participate if NONE is selected. "
                   "(Any of these reasons make the participant unable to take "
                   "part in the informed consent process)"),
    )

    hiv_status = models.CharField(
        verbose_name="Please tell me your current HIV status?",
        max_length=30,
        choices=VERBAL_HIVRESULT_CHOICE,
        help_text='If not HIV(+) participant is not elgiible.'
    )

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    is_consented = models.BooleanField(
        default=False,
        editable=False)

    is_refused = models.BooleanField(
        default=False,
        editable=False)

    loss_reason = models.TextField(
        verbose_name='Reason not eligible',
        max_length=500,
        null=True,
        editable=False,
        help_text='(stored for the loss form)')

    consent_datetime = models.DateTimeField(
        editable=False,
        null=True,
        help_text='filled from clinic_consent'
    )

    additional_key = models.CharField(
        max_length=36,
        verbose_name='-',
        editable=False,
        default=None,
        null=True,
        help_text=('A uuid to be added to clinic members to bypass the '
                   'unique constraint for firstname, initials, household_structure. '
                   'Always null for non-clinic members.'),
    )

    objects = EligibilityManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.screening_identifier,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.screening_identifier = ScreeningIdentifier().identifier
            self.update_subject_identifier_on_save()
        eligibility = Eligibility(
            age=self.age_in_years, literate=self.literacy,
            guardian=self.guardian, legal_marriage=self.legal_marriage,
            marriage_certificate=self.marriage_certificate,
            citizen=self.citizen, hiv_status=self.hiv_status,
            participation=self.inability_to_participate)
        self.is_eligible = eligibility.eligible
        self.loss_reason = eligibility.reasons
        self.update_mapper_fields
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} ({self.initials}) {self.gender}/{self.age_in_years}'

    def get_search_slug_fields(self):
        fields = ['screening_identifier']
        return fields

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
            self.subject_identifier_aka = self.subject_identifier_as_pk.hex
        return self.subject_identifier

    @property
    def registration_unique_field(self):
        return 'screening_identifier'

    @property
    def update_mapper_fields(self):
        mapper = site_mappers.registry.get(site_mappers.current_map_area)
        self.map_area = site_mappers.current_map_area
        self.center_lat = mapper.center_lat
        self.center_lon = mapper.center_lon

    class Meta:
        unique_together = [
            'screening_identifier', 'first_name', 'initials', 'additional_key']
