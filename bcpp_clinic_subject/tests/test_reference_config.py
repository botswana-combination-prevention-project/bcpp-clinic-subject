from django.test import TestCase
from edc_reference.reference_model_config import ReferenceModelConfig,\
    ReferenceFieldValidationError
from edc_reference.site import site_reference_configs


class TestReferenceConfig(TestCase):

    def test_site_validates_no_fields_raises(self):
        model = 'edc_reference.crfone'
        site_reference_configs.registry = {}
        self.assertRaises(
            ReferenceFieldValidationError,
            ReferenceModelConfig,
            fields=[],
            model=model)
