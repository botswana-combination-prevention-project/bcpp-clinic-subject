import arrow

from dateutil.tz import gettz
from datetime import datetime

from model_mommy import mommy

from django.test import TestCase

from bcpp_clinic_screening.tests import ScreeningTestHelper
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE
from edc_registration.models import RegisteredSubject

from ..models import Appointment, Enrollment


tzinfo = gettz('Africa/Gaborone')

clinic_v1 = Consent(
    'bcpp_clinic_subject.subjectconsent',
    version=1,
    start=arrow.get(
        datetime(2013, 10, 18, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2018, 4, 30, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=16,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE])

site_consents.register(clinic_v1)


class TestSubjectConsent(TestCase):

    screening_test_helper = ScreeningTestHelper()

    def test_create_consent_updates_registered_subject(self):
        """Test creating consent creates updates a registered subject.
        """
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
        subject_eligibility = self.screening_test_helper.make_eligibility()
        self.assertEqual(
            RegisteredSubject.objects.first().registration_identifier,
            subject_eligibility.eligibility_identifier)
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier=subject_eligibility.eligibility_identifier)
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
            eligibility_identifier=subject_eligibility.eligibility_identifier)
        self.assertEqual(Enrollment.objects.all().count(), 1)
        self.assertEqual(
            Enrollment.objects.first().subject_identifier, subject_consent.subject_identifier)

    def test_consent_creates_appointments(self):
        """Test enrollment created by a consent creates appointments.
        """
        subject_eligibility = self.screening_test_helper.make_eligibility()
        subject_consent = mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier=subject_eligibility.eligibility_identifier)
        self.assertEqual(Appointment.objects.all().count(), 1)
        self.assertEqual(
            Appointment.objects.first().subject_identifier, subject_consent.subject_identifier)
