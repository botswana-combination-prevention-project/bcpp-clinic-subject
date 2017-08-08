from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_consent.field_mixins import CitizenFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin

from ..eligibility_verifier import EligibilityVerifier
from ..managers import SubjectConsentManager


class SubjectConsent(ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
                     NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin,
                     SampleCollectionFieldsMixin, CitizenFieldsMixin,
                     VulnerabilityFieldsMixin, SearchSlugModelMixin,
                     BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    eligibility_verifier_cls = EligibilityVerifier

    screening_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=50,
        blank=True,
        unique=True)

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

    objects = SubjectConsentManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier, self.registration_identifier,)

    def __str__(self):
        return '{0} V{1}'.format(
            self.subject_identifier,
            self.version)

    def save(self, *args, **kwargs):
        self.registration_identifier = self.screening_identifier
        self.eligibility_verifier_cls(
            created=self.id,
            screening_identifier=self.screening_identifier,
            subject_identifier=self.subject_identifier)
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = ['subject_identifier']
        return fields

    class Meta(ConsentModelMixin.Meta):
        ordering = ('-created', )
