from django.test import TestCase, tag

from model_mommy import mommy

from bcpp_clinic_screening.tests import ScreeningTestHelper

from ..models import SubjectConsent
from ..models.questionnaire import Questionnaire
from ..model_wrappers import SubjectConsentModelWrapper, CrfModelWrapper
from .subject_helper import SubjectHelper


@tag('wrappers')
class TestWrappers(TestCase):

    subject_helper = SubjectHelper()
    screening_test_helper = ScreeningTestHelper()

    def test_consent_model_wrapper(self):
        wrapper = SubjectConsentModelWrapper(
            model_obj=SubjectConsent())
        self.assertIsNotNone(wrapper.href)

    def test_consent_model_wrapper_add(self):
        wrapper = SubjectConsentModelWrapper(model_obj=SubjectConsent())
        self.assertIn('add', wrapper.href)

    def test_consent_model_wrapper_change(self):
        options = {'identity': '12315678', 'confirm_identity': '12315678'}
        subject_eligibility = self.screening_test_helper.make_eligibility()
        model_obj = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            **options,
            screening_identifier=subject_eligibility.screening_identifier)
        wrapper = SubjectConsentModelWrapper(model_obj=model_obj)
        self.assertIn('change', wrapper.href)

    def test_crf_model_wrapper(self):
        wrapper = CrfModelWrapper(
            model_obj=Questionnaire())
        self.assertIsNotNone(wrapper.href)

    def test_crf_model_wrapper_add(self):
        wrapper = CrfModelWrapper(model_obj=Questionnaire())
        self.assertIn('add', wrapper.href)

    def test_crf_model_wrapper_change(self):
        subject_visit = self.subject_helper.complete_clinic_visit()
        model_obj = mommy.make_recipe(
            'bcpp_clinic_subject.questionnaire',
            subject_visit=subject_visit)
        wrapper = CrfModelWrapper(model_obj=model_obj)
        self.assertIn('change', wrapper.href)
