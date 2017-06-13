import arrow

from dateutil.tz import gettz
from datetime import datetime

from model_mommy import mommy

from django.test import TestCase

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

from ..models.appointment import Appointment
from bcpp_clinic_screening.models.subject_eligibility import SubjectEligibility
from edc_registration.models import RegisteredSubject

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

    def setUp(self):
        self.subject_eligibility = mommy.make_recipe(
            'bcpp_clinic_screening.subjecteligibility')

    def test_create_consent(self):
        """Test creating consent creates an appointment
        """
        self.assertEqual(SubjectEligibility.objects.all().count(), 1)
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
        mommy.make_recipe(
            'bcpp_clinic_subject.subjectconsent',
            eligibility_identifier=self.subject_eligibility.eligibility_identifier)
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
#         self.assertEqual(Appointment.objects.all().count(), 1)
