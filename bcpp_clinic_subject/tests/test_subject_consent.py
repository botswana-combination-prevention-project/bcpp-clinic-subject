import re
from django.db.utils import IntegrityError
from model_mommy import mommy

from django.test import TestCase, tag

from edc_base.utils import get_utcnow
# from edc_constants.constants import UUID_PATTERN

# from ..models import SubjectConsent, Enrollment
# from edc_registration.models import RegisteredSubject


class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_eligibility = mommy.make_recipe(
            'bcpp_clinic_screening.subjecteligibility')

    def test_cannot_create_consent_without_screening(self):
        """Test adding a consent without Clinic Eligibility first raises an
           Exception.
        """
        self.assertRaises(IntegrityError, mommy.make_recipe,
                          'bcpp_clinic_subject.subjectconsent',
                          consent_datetime=get_utcnow)
