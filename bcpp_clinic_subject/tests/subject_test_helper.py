from django.utils import timezone
from datetime import datetime

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO

from edc_constants.constants import POS, NOT_APPLICABLE, FEMALE

from ..constants import ABLE_TO_PARTICIPATE
from ..models import (
    SubjectEligibility, Appointment, SubjectConsent, SubjectVisit)


class SubjectTestHelper:

    def make_eligibility(self, options=None):
        """Returns subject eligibilty.
        """
        if options:
            options = options
        else:
            options = dict(
                report_datetime=get_utcnow(), age_in_years=27,
                part_time_resident=YES, first_name='TEST', initials='TT',
                gender=FEMALE, has_identity=YES, hiv_status=POS,
                inability_to_participate=ABLE_TO_PARTICIPATE, citizen=YES,
                literacy=YES, guardian=NOT_APPLICABLE)
        return SubjectEligibility.objects.create(**options)

    def clinic_visit(self):
        subject_eligibility = self.make_eligibility()
        options = {}
        options.update(
            study_site='40',
            consent_datetime=timezone.now(), dob=datetime(1989, 7, 7).date(),
            first_name='TEST', last_name='TEST', initials='TT', gender='M',
            identity='12315678', confirm_identity='12315678',
            may_store_samples=YES, is_dob_estimated='-', is_incarcerated=NO,
            is_literate=YES, identity_type='OMANG', marriage_certificate='N/A',
            screening_identifier=subject_eligibility.screening_identifier)
        subject_consent = SubjectConsent.objects.create(**options)

        appointment = Appointment.objects.get(
            subject_identifier=subject_consent.subject_identifier)
        return SubjectVisit.objects.create(
            report_datetime=timezone.now(), appointment=appointment)
