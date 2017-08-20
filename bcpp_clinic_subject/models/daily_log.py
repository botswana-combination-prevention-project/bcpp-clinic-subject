import arrow

from django.db import models

from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.utils import get_utcnow

from ..managers import DailyLogManager


class DailyLog(BaseUuidModel):
    """A model completed by the user daily to help measure the daily flow
    of patients in the clinic.
    """

    report_datetime = models.DateTimeField(default=get_utcnow)

    report_date = models.DateTimeField(
        null=True,
        unique=True,
        editable=False)

    from_pharma = models.IntegerField(
        verbose_name='Number of patients referred from pharmacy')

    from_nurse_prescriber = models.IntegerField(
        verbose_name='Number of patients referred from nurse prescriber')

    from_ssc = models.IntegerField(
        verbose_name='Number of patients referred from SSC')

    from_other = models.IntegerField(
        verbose_name='Number of patients referred from \'other\'')

    idcc_scheduled = models.IntegerField(
        verbose_name='Number of patients scheduled/booked for appointments '
        'in the IDCC')

    idcc_newly_registered = models.IntegerField(
        verbose_name='Number of patients newly registered to the IDCC')

    idcc_no_shows = models.IntegerField(
        verbose_name='Number of patients who did not show up for '
        'their appointment.')

    approached = models.IntegerField(
        verbose_name='Number of patients approached')

    refused = models.IntegerField(
        verbose_name='Number of patients who refused to complete the '
        'eligibility checklist')

    objects = DailyLogManager()

    history = HistoricalRecords()

    def __str__(self):
        return self.report_date.strftime('%Y-%m-%d')

    def natural_key(self):
        return (self.report_date, self.hostname_created,)

    def save(self, *args, **kwargs):
        self.report_date = arrow.Arrow.from_datetime(
            self.report_datetime).date()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['report_date', 'hostname_created']
