# from django.test import TestCase, tag
#
# from edc_base.utils import get_utcnow
# from edc_constants.constants import YES, FEMALE, POS, NOT_APPLICABLE, NEG
# from edc_registration.models import RegisteredSubject
#
# from ..constants import ABLE_TO_PARTICIPATE
# from ..models import SubjectEligibility
# from .screening_tests_helper import ScreeningTestHelper
#
#
# class TestCreateClinicEligibility(TestCase):
#
#     screening_test_helper = ScreeningTestHelper()
#
#     @tag('eligibility_creation')
#     def test_subject_eligibility(self):
#         """Test create subject eligibilty.
#         """
#         self.screening_test_helper.make_eligibility()
#         self.assertEqual(SubjectEligibility.objects.all().count(), 1)
#
#     def test_create_registered_subject(self):
#         """Test subject eligibilty creates registered subject.
#         """
#         self.screening_test_helper.make_eligibility()
#         self.assertEqual(RegisteredSubject.objects.all().count(), 1)
#
#     def test_create_registered_subject_2(self):
#         """Test created registered subject matches the the subject eligibility.
#         """
#         subject_eligibility = self.screening_test_helper.make_eligibility()
#         registered_subject = RegisteredSubject.objects.first()
#         self.assertEqual(
#             registered_subject.registration_identifier,
#             subject_eligibility.screening_identifier)
#         self.assertEqual(
#             registered_subject.registration_identifier,
#             subject_eligibility.registration_identifier)
#         self.assertEqual(
#             registered_subject.screening_identifier,
#             subject_eligibility.screening_identifier)
#
#     def test_is_eligible_true(self):
#         """Test subject eligibility is_eligible is True.
#         """
#         options = dict(
#             report_datetime=get_utcnow(),
#             age_in_years=27,
#             part_time_resident=YES,
#             first_name='TEST',
#             initials='TT',
#             gender=FEMALE,
#             has_identity=YES,
#             hiv_status=POS,
#             inability_to_participate=ABLE_TO_PARTICIPATE,
#             citizen=YES,
#             literacy=YES,
#             guardian=NOT_APPLICABLE)
#         subject_eligibility = self.screening_test_helper.make_eligibility(
#             options=options)
#         self.assertTrue(subject_eligibility.is_eligible)
#
#     def test_is_eligible_false(self):
#         """Test subject eligibility is_eligible is False.
#         """
#         options = dict(
#             report_datetime=get_utcnow(),
#             age_in_years=27,
#             part_time_resident=YES,
#             first_name='TEST',
#             initials='TT',
#             gender=FEMALE,
#             has_identity=YES,
#             hiv_status=NEG,
#             inability_to_participate=ABLE_TO_PARTICIPATE,
#             citizen=YES,
#             literacy=YES,
#             guardian=NOT_APPLICABLE)
#         subject_eligibility = self.screening_test_helper.make_eligibility(
#             options=options)
#         self.assertFalse(subject_eligibility.is_eligible)
