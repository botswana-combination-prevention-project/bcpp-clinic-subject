import uuid

from django.db import models

from edc_base.model_mixins.base_uuid_model import BaseUuidModel

from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.field_mixins import CitizenFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin

from edc_constants.choices import YES_NO

from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin as BaseUpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugModelMixin
from edc_registration.exceptions import RegisteredSubjectError
from bcpp_clinic_screening.models.subject_eligibility import SubjectEligibility
from bcpp_clinic_screening.exceptions import ElibilityError

from .enrollment import Enrollment


class UpdateOrCreateEnrollment:
    """Update or creates an enrollement after consent is created.
    """

    def update_or_create_enrollment(self, subject_eligibility):
        """Updates or creates an enrollment.
        """
        try:
            Enrollment.objects.get(
                subject_identifier=self.subject_identifier,
                visit_schedule_name=Enrollment._meta.visit_schedule_name)
        except Enrollment.DoesNotExist:
            Enrollment.objects.create(
                subject_identifier=self.subject_identifier,
                consent_identifier=self.consent_identifier,
                is_eligible=subject_eligibility.is_eligible)


class UpdatesOrCreatesRegistrationModelMixin(BaseUpdatesOrCreatesRegistrationModelMixin):

    @property
    def registration_unique_field(self):
        return 'registration_identifier'

    def registration_raise_on_illegal_value_change(self, registered_subject):
        """Raises an exception if a value changes between
        updates.
        """
        pass
#         if registered_subject.identity != self.identity:
#             raise RegisteredSubjectError(
#                 'Identity may not be changed. Expected {}. Got {}'.format(
#                     registered_subject.identity,
#                     self.identity))
#         if (registered_subject.registration_identifier
#             and uuid.UUID(registered_subject.registration_identifier) !=
#                 self.household_member.internal_identifier):
#             raise RegisteredSubjectError(
#                 'Internal Identifier may not be changed. Expected {}. '
#                 'Got {}'.format(
#                     registered_subject.registration_identifier,
#                     self.household_member.internal_identifier))
#         if registered_subject.dob != self.dob:
#             raise RegisteredSubjectError(
#                 'DoB may not be changed. Expected {}. Got {}'.format(
#                     registered_subject.dob,
#                     self.dob))

    class Meta:
        abstract = True


class SubjectConsent(ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
                     NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin,
                     SampleCollectionFieldsMixin, CitizenFieldsMixin,
                     VulnerabilityFieldsMixin, SearchSlugModelMixin,
                     UpdateOrCreateEnrollment, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    eligibility_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    registration_identifier = models.CharField(
        verbose_name='Registration Identifier',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    is_minor = models.CharField(
        verbose_name=("Is subject a minor?"),
        max_length=10,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text=('Subject is a minor if aged 16-17. A guardian must '
                   'be present for consent. HIV status may NOT be '
                   'revealed in the household.'),
        editable=False)

    is_signed = models.BooleanField(
        default=False,
        editable=False)

    lab_identifier = models.CharField(
        verbose_name=("lab allocated identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

    htc_identifier = models.CharField(
        verbose_name=("HTC Identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

    pims_identifier = models.CharField(
        verbose_name=("PIMS identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

    def __str__(self):
        return '{0} V{1}'.format(
            self.subject_identifier,
            self.version)

    def save(self, *args, **kwargs):
        self.registration_identifier = self.eligibility_identifier
        super().save(*args, **kwargs)

    class Meta(ConsentModelMixin.Meta):
        verbose_name = 'Clinic Consent RBD'
        verbose_name_plural = 'Clinic Consent RBD'
        ordering = ('-created', )
