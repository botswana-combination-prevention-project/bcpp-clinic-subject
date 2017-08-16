from django.test import TestCase

from edc_constants.constants import YES, POS, NO, OTHER

from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import RequisitionMetadata, CrfMetadata


from ..constants import (
    INITIATION, VIRAL_LOAD, MASA_VL_SCHEDULED, RESEARCH_BLOOD_DRAW)
from ..models.questionnaire import Questionnaire
from ..models.viral_load_tracking import ViralLoadTracking
from .subject_test_helper import SubjecTesttHelper


class TestRuleGroups(TestCase):

    subject_test_helper = SubjecTesttHelper()

    def setUp(self):
        self.subject_visit = self.subject_test_helper.clinic_visit()

    def test_clinic_viral_load_required(self):
        """Assert viral load is required if registration type is INITIATION.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=INITIATION,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    def test_clinic_viral_load_required1(self):
        """Assert viral load is required if registration type is OTHER.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=OTHER,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    def test_clinic_viral_load_not_required(self):
        """Assert viral load not required if not initiation or other.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=MASA_VL_SCHEDULED,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            panel_name=VIRAL_LOAD,
            entry_status=NOT_REQUIRED)
        self.assertEqual(reqs.count(), 1)

    def test_clinic_rbd_required(self):
        """Assert viral load not required if not initiation or other.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=MASA_VL_SCHEDULED,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        reqs = RequisitionMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            panel_name=RESEARCH_BLOOD_DRAW,
            entry_status=REQUIRED)
        self.assertEqual(reqs.count(), 1)

    def test_clinic_vlloadtracking(self):
        """Assert viralloadtracking is required on registration type is
        MASA_VL_SCHEDULED.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=MASA_VL_SCHEDULED,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            model='bcpp_clinic_subject.viralloadtracking',
            entry_status=REQUIRED)
        self.assertEqual(crf.count(), 1)

    def test_clinic_vlloadtracking1(self):
        """Assert viralloadtracking not required if not MASA_VL_SCHEDULED.
        """
        Questionnaire.objects.create(
            subject_visit=self.subject_visit,
            registration_type=OTHER,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            model='bcpp_clinic_subject.viralloadtracking',
            entry_status=NOT_REQUIRED)
        self.assertEqual(crf.count(), 1)

    def test_clinic_vl_result(self):
        """Assert vlresult is required on is_drawn is YES.
        """
        ViralLoadTracking.objects.create(
            subject_visit=self.subject_visit,
            is_drawn=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            model='bcpp_clinic_subject.vlresult',
            entry_status=REQUIRED)
        self.assertEqual(crf.count(), 1)

    def test_clinic_vl_result1(self):
        """Assert vlresult not required on is_drawn is NO.
        """
        ViralLoadTracking.objects.create(
            subject_visit=self.subject_visit,
            is_drawn=NO)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            model='bcpp_clinic_subject.vlresult',
            entry_status=NOT_REQUIRED)
        self.assertEqual(crf.count(), 1)

    def test_clinic_viral_load1(self):
        """Assert viralload required on is_drawn is YES.
        """
        ViralLoadTracking.objects.create(
            subject_visit=self.subject_visit,
            is_drawn=YES)

        crf = CrfMetadata.objects.filter(
            subject_identifier=self.subject_visit.subject_identifier,
            model='bcpp_clinic_subject.vlresult',
            entry_status=REQUIRED)
        self.assertEqual(crf.count(), 1)
