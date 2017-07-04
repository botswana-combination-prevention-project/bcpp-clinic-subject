from model_mommy import mommy

from django.test import TestCase

from bcpp_clinic_screening.tests import ScreeningTestHelper
from edc_registration.models import RegisteredSubject

from ..models import Appointment, Enrollment


class TestSubjectConsent(TestCase):

    screening_test_helper = ScreeningTestHelper()

    def test_create_consent_updates_registered_subject(self):
        """Test creating consent creates updates a registered subject.
        """
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
        subject_eligibility = self.screening_test_helper.make_eligibility()
        self.assertEqual(
            RegisteredSubject.objects.first().registration_identifier,
            subject_eligibility.screening_identifier)
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            screening_identifier=subject_eligibility.screening_identifier)
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
        self.assertEqual(
            RegisteredSubject.objects.first().subject_identifier,
            subject_consent.subject_identifier)

    def test_consent_creates_enrollment(self):
        """Test enrollment created when a consent is created.
        """
        subject_eligibility = self.screening_test_helper.make_eligibility()
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            screening_identifier=subject_eligibility.screening_identifier)
        self.assertEqual(Enrollment.objects.all().count(), 1)
        self.assertEqual(
            Enrollment.objects.first().subject_identifier, subject_consent.subject_identifier)

    def test_consent_creates_appointments(self):
        """Test enrollment created by a consent creates appointments.
        """
        subject_eligibility = self.screening_test_helper.make_eligibility()
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            screening_identifier=subject_eligibility.screening_identifier)
        self.assertEqual(Appointment.objects.all().count(), 1)
        self.assertEqual(
            Appointment.objects.first().subject_identifier, subject_consent.subject_identifier)
