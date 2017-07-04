from django.utils import timezone
from datetime import datetime

from edc_visit_tracking.constants import SCHEDULED
from bcpp_clinic_screening.tests import ScreeningTestHelper

from ..models import Appointment, SubjectConsent, SubjectVisit
from edc_constants.constants import YES, NO


class SubjectHelper:

    screening_test_helper = ScreeningTestHelper()

    def complete_clinic_visit(self):
        subject_eligibility = self.screening_test_helper.make_eligibility()
        options = {}
        options.update(
            study_site='40',
            consent_datetime=timezone.now(),
            dob=datetime(1989, 7, 7).date(),
            first_name='TEST',
            last_name='TEST',
            initials='TT',
            gender='M',
            identity='12315678',
            confirm_identity='12315678',
            may_store_samples=YES,
            is_dob_estimated='-',
            is_incarcerated=NO,
            is_literate=YES,
            identity_type='OMANG',
            marriage_certificate='N/A',
            screening_identifier=subject_eligibility.screening_identifier)
        subject_consent = SubjectConsent.objects.create(**options)

        appointment = Appointment.objects.get(
            subject_identifier=subject_consent.subject_identifier)
        return SubjectVisit.objects.create(
            report_datetime=timezone.now(), appointment=appointment,
            reason=SCHEDULED)
