from django.db import models
from django.utils import timezone

from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_visit_schedule.model_mixins import EnrollmentModelMixin

from ..managers import EnrollmentManager


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by the
    Clinic Consents.
    """

    ADMIN_SITE_NAME = 'bcpp_clinic_subject_admin'

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    consent_identifier = models.UUIDField()

    report_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False)

    objects = EnrollmentManager()

    history = HistoricalRecords()

    class Meta(EnrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule1.schedule1'
