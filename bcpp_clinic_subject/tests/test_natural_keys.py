from django.test import TestCase, tag

from bcpp_clinic_screening.models import SubjectEligibility
from edc_constants.constants import YES, POS
from edc_sync.tests.sync_test_helper import SyncTestHelper

from ..models import SubjectConsent, SubjectVisit, Enrollment, Questionnaire
from ..constants import INITIATION
from .test_clinic_mixin import TestClinicMixin
from .subject_helper import SubjectHelper


@tag('natural_key')
class TestNaturalKey(TestClinicMixin, TestCase):

    sync_helper = SyncTestHelper()
    subject_helper = SubjectHelper()

    def test_natural_key_attrs(self):
        self.sync_helper.sync_test_natural_key_attr('bcpp_clinic_subject')

    def test_get_by_natural_key_attr(self):
        self.sync_helper.sync_test_get_by_natural_key_attr(
            'bcpp_clinic_subject')

    def test_managers(self):
        self.subject_helper.complete_clinic_visit()
        models = [
            SubjectEligibility, SubjectConsent, SubjectVisit, Enrollment]
        for model in models:
            obj = model.objects.first()
            self.assertTrue(model.objects.get_by_natural_key(
                *obj.natural_key()))

    @tag('crf_manager')
    def test_managers_crf(self):
        subject_visit = self.subject_helper.complete_clinic_visit()
        obj = Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=INITIATION,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)
        self.assertTrue(Questionnaire.objects.get_by_natural_key(
            *obj.natural_key()))
