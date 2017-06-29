from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED

from bcpp_clinic_screening.tests import ScreeningTestHelper

from ..models.appointment import Appointment
from ..models.subject_visit import SubjectVisit


class SubjectHelper:

    screening_test_helper = ScreeningTestHelper()

    def complete_clinic_visit(self):
        eligibility = self.screening_test_helper.make_eligibility()
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier=eligibility.eligibility_identifier)
        appointment = Appointment.objects.get(
            subject_identifier=subject_consent.subject_identifier)
        return SubjectVisit.objects.create(
            report_datetime=get_utcnow(), appointment=appointment,
            reason=SCHEDULED)
