from django.test import TestCase, tag

from ..views import SubjectConsentModelWrapper
from ..models import SubjectConsent
from model_mommy import mommy


@tag('wrappers')
class TestWrappers(TestCase):

    def test_household_model_wrapper(self):
        wrapper = SubjectConsentModelWrapper(
            model_obj=SubjectConsent())
        self.assertIsNotNone(wrapper.href)

    def test_household_model_wrapper_add(self):
        wrapper = SubjectConsentModelWrapper(model_obj=SubjectConsent())
        self.assertIn('add', wrapper.href)

    def test_household_model_wrapper_change(self):
        model_obj = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier='1234')
        wrapper = SubjectConsentModelWrapper(model_obj=model_obj)
        self.assertIn('change', wrapper.href)
        self.assertIn(model_obj.pk, wrapper.href)
