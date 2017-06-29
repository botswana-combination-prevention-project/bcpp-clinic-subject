from django.test import TestCase, tag

from .test_clinic_mixin import TestClinicMixin
from bcpp_clinic_screening.models.subject_eligibility import SubjectEligibility
from bcpp_clinic_subject.models.subject_consent import SubjectConsent
from bcpp_clinic_subject.models.subject_visit import SubjectVisit
from bcpp_clinic_subject.tests.subject_helper import SubjectHelper


@tag('test_mixin')
class TestMixin(TestCase, TestClinicMixin):
    """ Enroll eligible member into a clinic. Complete Subject Eligibility,
    Subject Consent and Subject Visit.
    """

    subject_helper = SubjectHelper()

    def test_subject_eligibility(self):
        """ Assert eligible subject eligibility.
        """
        self.complete_clinic_visit()
        self.assertEqual(
            SubjectEligibility.objects.filter(is_eligible=True).count(), 1)

    def test_subject_consent(self):
        """ Assert subject consent is completed.
        """
        self.complete_clinic_visit()
        self.assertEqual(
            SubjectConsent.objects.all().count(), 1)

    def test_subject_visit(self):
        """ Assert subject visit is completed.
        """
        self.complete_clinic_visit()
        self.assertEqual(
            SubjectVisit.objects.all().count(), 1)
