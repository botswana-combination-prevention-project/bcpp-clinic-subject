from django.test import TestCase, tag
from edc_reference.reference_model_config import ReferenceModelConfig,\
    ReferenceFieldValidationError
from edc_reference.site import site_reference_configs
from bcpp_clinic_subject.models.questionnaire import Questionnaire
from model_mommy import mommy


@tag('1')
class TestReferenceConfig(TestCase):

    def test_questionnare_reference(self):
        mommy.make_recipe('bcpp_clinic_subject.questionnaire')
