from django.test import TestCase, tag
from ..eligibility_verifier import EligibilityVerifier


class TestEligibilityVerifier(TestCase):

    @tag('2')
    def test_verifier(self):
        EligibilityVerifier()
