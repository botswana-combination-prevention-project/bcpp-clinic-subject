from django.test import TestCase

from ..models import SubjectConsent, SubjectVisit, SubjectEligibility
from .subject_test_helper import SubjectTestHelper


class TestSubjecTestHelper(TestCase):
    """ Enroll eligible member into a clinic. Complete Subject Eligibility,
    Subject Consent and Subject Visit.
    """

    subject_helper = SubjectTestHelper()

    def test_create_subject(self):
        """ Assert creating a consented subject.
        """
        self.subject_helper.clinic_visit()
        self.assertEqual(
            SubjectEligibility.objects.all().count(), 1)
        self.assertEqual(
            SubjectConsent.objects.all().count(), 1)
        self.assertEqual(
            SubjectVisit.objects.all().count(), 1)
