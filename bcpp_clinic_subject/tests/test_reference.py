from django.test import TestCase
from edc_reference.site import site_reference_configs


class TestReference(TestCase):

    def test(self):
        site_reference_configs.validate()
