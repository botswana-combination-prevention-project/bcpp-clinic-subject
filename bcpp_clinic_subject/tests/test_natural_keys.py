from django.test import TestCase, tag

from edc_sync.test_mixins import SyncTestSerializerMixin
from edc_constants.constants import YES, POS

from bcpp_clinic_screening.models import SubjectEligibility

from ..models import SubjectConsent, SubjectVisit, Enrollment, Questionnaire
from ..constants import INITIATION
from .test_clinic_mixin import TestClinicMixin


@tag('natural_key')
class TestNaturalKey(SyncTestSerializerMixin, TestClinicMixin, TestCase):

    def test_natural_key_attrs(self):
        self.sync_test_natural_key_attr('bcpp_clinic_subject')

    def test_get_by_natural_key_attr(self):
        self.sync_test_get_by_natural_key_attr('bcpp_clinic_subject')

    def test_managers(self):
        self.complete_clinic_visit()
        models = [
            SubjectEligibility, SubjectConsent, SubjectVisit, Enrollment]
        for model in models:
            obj = model.objects.first()
            self.assertTrue(model.objects.get_by_natural_key(
                *obj.natural_key()))

    @tag('crf_manager')
    def test_managers_crf(self):
        subject_visit = self.complete_clinic_visit()
        obj = Questionnaire.objects.create(
            subject_visit=subject_visit,
            registration_type=INITIATION,
            know_hiv_status=YES,
            current_hiv_status=POS,
            arv_evidence=YES)
        self.assertTrue(Questionnaire.objects.get_by_natural_key(
            *obj.natural_key()))
