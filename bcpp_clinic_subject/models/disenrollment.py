from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin

from ..managers import DisenrollmentManager


class Disenrollment(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    ADMIN_SITE_NAME = 'bcpp_clinic_subject_admin'

    objects = DisenrollmentManager()

    history = HistoricalRecords()

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule1.schedule1'
