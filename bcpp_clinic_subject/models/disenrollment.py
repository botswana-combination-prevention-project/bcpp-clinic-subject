from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin

from ..managers import DisenrollmentManager


class Disenrollment(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    ADMIN_SITE_NAME = 'bcpp_clinic_subject_admin'

    objects = DisenrollmentManager()

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'subject_visit_schedule.schedule1'
        consent_model = 'bcpp_clinic_subject.subjectconsent'
