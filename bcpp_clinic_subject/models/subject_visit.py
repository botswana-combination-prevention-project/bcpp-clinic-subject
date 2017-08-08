from django.db import models

from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.creates.creates_metadata_model_mixin import CreatesMetadataModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins.visit_model_mixin import VisitModelMixin


from ..choices import VISIT_UNSCHEDULED_REASON
from ..constants import RESEARCH_BLOOD_DRAW
from .appointment import Appointment


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin,
                   RequiresConsentMixin, BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=25,
        blank=True,
        null=True,
        choices=VISIT_UNSCHEDULED_REASON,
    )

    objects = VisitModelManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.info_source = 'subject'
        self.reason = RESEARCH_BLOOD_DRAW
        self.appointment.appt_type = 'clinic'
        self.subject_identifier = self.appointment.subject_identifier
        super(SubjectVisit, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} {} ({}) {}'.format(self.appointment.subject_identifier,
                                      self.appointment.registered_subject.first_name,
                                      self.appointment.registered_subject.gender,
                                      self.appointment.visit_definition.code)
