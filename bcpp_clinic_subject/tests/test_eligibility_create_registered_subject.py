from django.test import TestCase

from edc_registration.models import RegisteredSubject

from .subject_test_helper import SubjectTestHelper


class TestEligibilityCreateRegisteredSubject(TestCase):

    subject_test_helper = SubjectTestHelper()

    def test_create_registered_subject(self):
        """Test subject eligibilty creates registered subject.
        """
        self.subject_test_helper.make_eligibility()
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)

    def test_create_registered_subject_2(self):
        """Test created registered subject matches the the subject eligibility.
        """
        subject_eligibility = self.subject_test_helper.make_eligibility()
        registered_subject = RegisteredSubject.objects.first()
        self.assertEqual(
            registered_subject.registration_identifier,
            subject_eligibility.screening_identifier)
        self.assertEqual(
            registered_subject.screening_identifier,
            subject_eligibility.screening_identifier)
