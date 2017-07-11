import arrow

from dateutil.tz import gettz
from datetime import datetime

from django.test import TestCase, tag

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

from bcpp_clinic_screening.models import SubjectEligibility

from ..models.subject_consent import SubjectConsent
from ..models.subject_visit import SubjectVisit
from ..tests.subject_helper import SubjectHelper

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


@tag('test_mixin')
class TestMixin(TestCase):
    """ Enroll eligible member into a clinic. Complete Subject Eligibility,
    Subject Consent and Subject Visit.
    """

    subject_helper = SubjectHelper()

    def test_subject_eligibility(self):
        """ Assert eligible subject eligibility, consent and visit completed.
        """
        self.subject_helper.complete_clinic_visit()
        self.assertEqual(
            SubjectEligibility.objects.filter(is_eligible=True).count(), 1)
        self.assertEqual(
            SubjectConsent.objects.all().count(), 1)
        self.assertEqual(
            SubjectVisit.objects.all().count(), 1)
