from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow

from .subject_eligibility import SubjectEligibility


class EnrollmentLossManager(models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(
            subject_eligibility__screening_identifier=screening_identifier
        )


class EnrollmentLoss(BaseUuidModel):
    """A system model auto created that captures the reason
    for a present BHS eligible member who passes BHS eligibility
    but is not participating in the BHS.
    """

    subject_eligibility = models.OneToOneField(
        SubjectEligibility, on_delete=models.PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name='Report date',
        default=get_utcnow,
        validators=[datetime_not_future])

    reason = models.TextField(
        verbose_name='Reason not eligible',
        max_length=500,
        help_text='Do not include any personal identifiable information.')

    objects = EnrollmentLossManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_eligibility.natural_key(),)

    class Meta:
        verbose_name_plural = "Enrollment Loss"
