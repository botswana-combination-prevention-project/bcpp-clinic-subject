from model_mommy import mommy

from django.test import TestCase, tag
from django.utils import timezone


from edc_constants.constants import MALE, NOT_APPLICABLE, YES, POS, NO, OTHER

from edc_base.utils import get_utcnow
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import RequisitionMetadata, CrfMetadata
from edc_visit_tracking.constants import SCHEDULED

from bcpp_clinic_screening.constants import ABLE_TO_PARTICIPATE
from bcpp_clinic_screening.models import SubjectEligibility

from ..constants import INITIATION, VIRAL_LOAD, MASA_VL_SCHEDULED
from ..models.appointment import Appointment
from ..models.questionnaire import Questionnaire
from ..models.subject_visit import SubjectVisit
from ..models.viral_load_tracking import ViralLoadTracking


@tag('rules')
class TestRuleGroups(TestCase):

    def complete_clinic_visit(self):
        def make_eligibility():
            options = dict(
                report_datetime=timezone.now(),
                part_time_resident=YES,
                initials='TT',
                gender=MALE,
                has_identity=YES,
                hiv_status=POS,
                inability_to_participate=ABLE_TO_PARTICIPATE,
                citizen=YES,
                literacy=YES,
                guardian=NOT_APPLICABLE,
                age_in_years=27)
            eligibility = SubjectEligibility.objects.create(**options)
            self.assertTrue(eligibility.is_eligible)
            return eligibility
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier=make_eligibility().eligibility_identifier)
        appointment = Appointment.objects.get(
            subject_identifier=subject_consent.subject_identifier)
        return SubjectVisit.objects.create(
            report_datetime=get_utcnow(), appointment=appointment,
            reason=SCHEDULED)

    @tag('vl_required')
    def test_clinic_viral_load_required(self):
        """Assert viral load is required if registration type is INITIATION.
        """
        subject_visit = self.complete_clinic_visit()
        Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=INITIATION,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    @tag('vl_required')
    def test_clinic_viral_load_required1(self):
        """Assert viral load is required if registration type is OTHER.
        """
        subject_visit = self.complete_clinic_visit()
        Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=OTHER,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    @tag('vl_not_required')
    def test_clinic_viral_load_not_required(self):
        """Assert viral load not required if not initiation or other.
        """
        subject_visit = self.complete_clinic_visit()
        Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=MASA_VL_SCHEDULED,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=NOT_REQUIRED)
        self.assertEqual(reqs.count(), 1)

    @tag('vl_tracking')
    def test_clinic_vlloadtracking(self):
        """Assert viralloadtracking is required on registration type is
        MASA_VL_SCHEDULED.
        """
        subject_visit = self.complete_clinic_visit()
        Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=MASA_VL_SCHEDULED,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            model='bcpp_clinic_subject.viralloadtracking',
            entry_status=REQUIRED)
        self.assertEqual(crf.count(), 1)

    @tag('vl_tracking')
    def test_clinic_vlloadtracking1(self):
        """Assert viralloadtracking not required if not MASA_VL_SCHEDULED.
        """
        subject_visit = self.complete_clinic_visit()
        Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=OTHER,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            model='bcpp_clinic_subject.viralloadtracking',
            entry_status=NOT_REQUIRED)
        self.assertEqual(crf.count(), 1)

    @tag('vl_result')
    def test_clinic_vl_result(self):
        """Assert vlresult is required on is_drawn is YES.
        """
        subject_visit = self.complete_clinic_visit()
        ViralLoadTracking.objects.create(
            subject_visit=subject_visit,
            is_drawn=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            model='bcpp_clinic_subject.vlresult',
            entry_status=REQUIRED)
        self.assertEqual(crf.count(), 1)

    @tag('vl_result')
    def test_clinic_vl_result1(self):
        """Assert vlresult not required on is_drawn is NO.
        """
        subject_visit = self.complete_clinic_visit()
        ViralLoadTracking.objects.create(
            subject_visit=subject_visit,
            is_drawn=NO)

        crf = CrfMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            model='bcpp_clinic_subject.vlresult',
            entry_status=NOT_REQUIRED)
        self.assertEqual(crf.count(), 1)

    @tag('viralload')
    def test_clinic_viral_load(self):
        """Assert viralload is required on is_drawn is NO.
        """
        subject_visit = self.complete_clinic_visit()
        ViralLoadTracking.objects.create(
            subject_visit=subject_visit,
            is_drawn=NO)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    @tag('viralload')
    def test_clinic_viral_load1(self):
        """Assert viralload not required on is_drawn is YES.
        """
        subject_visit = self.complete_clinic_visit()
        ViralLoadTracking.objects.create(
            subject_visit=subject_visit,
            is_drawn=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=NOT_REQUIRED)
        self.assertEqual(reqs.count(), 1)
