from django.db import models
from django.utils import timezone

from edc_visit_schedule.model_mixins import EnrollmentModelMixin
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_appointment.model_mixins import CreateAppointmentsMixin


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by the
    Clinic Consents.
    """

    ADMIN_SITE_NAME = 'clinic_subject_admin'

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    consent_identifier = models.UUIDField()

    report_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False)

    class Meta:
        visit_schedule_name = 'clinic_visit_schedule.schedule1'
        consent_model = 'clinic_subject.subjectconsent'
        verbose_name = 'Enrollment Clinic'
        verbose_name_plural = 'Enrollment Clinic'
