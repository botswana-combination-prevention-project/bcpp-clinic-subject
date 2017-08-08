# import unittest
#
# from django.apps import apps as django_apps
# from django.test import tag
#
# from edc_constants.constants import (
#     YES, NO, POS, NEG, IND, UNK, NOT_APPLICABLE, OTHER)
#
# from ..eligibility import (
#     AgeEvaluator, CitizenshipEvaluator, ParticipationEvaluator,
#     LiteracyEvaluator, Eligibility, HivStatusEvaluator)
#
# from ..constants import ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY
#
#
# @tag('eligibility')
# class TestClinicEligibility(unittest.TestCase):
#
#     def test_eligibility_invalid_age_in_years(self):
#         app_config = django_apps.get_app_config('bcpp_clinic_screening')
#
#         age_evaluator = AgeEvaluator(
#             age=app_config.eligibility_age_adult_lower - 1)
#         self.assertFalse(age_evaluator.eligible)
#
#         age_evaluator = AgeEvaluator(
#             age=app_config.eligibility_age_adult_lower)
#         self.assertTrue(age_evaluator.eligible)
#
#         age_evaluator = AgeEvaluator(
#             age=app_config.eligibility_age_adult_upper)
#         self.assertTrue(age_evaluator.eligible)
#
#         age_evaluator = AgeEvaluator(
#             age=app_config.eligibility_age_adult_upper + 1)
#         self.assertFalse(age_evaluator.eligible)
#
#     def test_eligibility_invalid_age_in_years_reasons(self):
#         age_evaluator = AgeEvaluator(age=15)
#         self.assertIn('age<18', age_evaluator.reason)
#         age_evaluator = AgeEvaluator(age=100)
#         self.assertIn('age>64', age_evaluator.reason)
#
#     def test_eligibility_age_minor_with_guardian(self):
#         """Assert eligibility criteria is True if for a minor
#             guardian is provided.
#         """
#         age_evaluator = AgeEvaluator(age=16, guardian=YES)
#         self.assertTrue(age_evaluator.eligible)
#         age_evaluator = AgeEvaluator(age=17, guardian=YES)
#         self.assertTrue(age_evaluator.eligible)
#
#     def test_eligibility_age_minor_no_guardian(self):
#         """Assert eligibility criteria is False if for a minor no guardian.
#         """
#         age_evaluator = AgeEvaluator(age=16, guardian=NO)
#         self.assertFalse(age_evaluator.eligible)
#         age_evaluator = AgeEvaluator(age=17, guardian=NO)
#         self.assertFalse(age_evaluator.eligible)
#
#     def test_eligibility_age_minor_no_guardian2(self):
#         """Assert eligibility criteria is False if for a minor no guardian.
#         """
#         age_evaluator = AgeEvaluator(age=16, guardian=NOT_APPLICABLE)
#         self.assertFalse(age_evaluator.eligible)
#         age_evaluator = AgeEvaluator(age=17, guardian=NOT_APPLICABLE)
#         self.assertFalse(age_evaluator.eligible)
#
#     def test_eligibility_citizen(self):
#         """Assert not a citizen, not legally married to a citizen,
#         is not eligible.
#         """
#         citizenship_evaluator = CitizenshipEvaluator(citizen=YES)
#         self.assertTrue(citizenship_evaluator.eligible)
#
#     def test_eligibility_participation(self):
#         """Assert participation eligibility is true if able to participate.
#         """
#         participation_evaluator = ParticipationEvaluator(
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(participation_evaluator.eligible)
#
#     def test_eligibility_participation_metaly_incapacity(self):
#         """Assert participation eligibility is False if metaly incapacity.
#         """
#         participation_evaluator = ParticipationEvaluator(
#             participation=MENTAL_INCAPACITY)
#         self.assertFalse(participation_evaluator.eligible)
#
#     def test_eligibility_participation_deaf_mute(self):
#         """Assert participation eligibility is false if Too sick.
#         """
#         participation_evaluator = ParticipationEvaluator(
#             participation='Too sick')
#         self.assertFalse(participation_evaluator.eligible)
#
#     def test_eligibility_participation_too_sick(self):
#         """Assert participation eligibility is false if Deaf/Mute.
#         """
#         participation_evaluator = ParticipationEvaluator(
#             participation='Deaf/Mute')
#         self.assertFalse(participation_evaluator.eligible)
#
#     def test_eligibility_participation_incarcerated(self):
#         """Assert participation eligibility is false if Incarcerated.
#         """
#         participation_evaluator = ParticipationEvaluator(
#             participation='Incarcerated')
#         self.assertFalse(participation_evaluator.eligible)
#
#     def test_eligibility_not_acitizen(self):
#         """Assert not a citizen, not legally married to a citizen, is not eligible.
#         """
#         citizenship_evaluator = CitizenshipEvaluator(
#             citizen=NO, legal_marriage=NO)
#         self.assertFalse(citizenship_evaluator.eligible)
#
#     def test_eligibility_not_acitizen1(self):
#         """Assert not a citizen, legal married to a citizen and has marriage
#         certificate is eligible.
#         """
#         citizenship_evaluator = CitizenshipEvaluator(
#             citizen=NO, marriage_certificate=YES, legal_marriage=YES)
#         self.assertTrue(citizenship_evaluator.eligible)
#
#     def test_eligibility_not_acitizen2(self):
#         """Assert not a citizen, legal married to a citizen and has marriage
#         certificate is eligible.
#         """
#         citizenship_evaluator = CitizenshipEvaluator(
#             citizen=NO, marriage_certificate=NO, legal_marriage=YES)
#         self.assertFalse(citizenship_evaluator.eligible)
#
#     def test_eligibility_literacy(self):
#         """Assert literate participant is eligible.
#         """
#         literacy_evaluator = LiteracyEvaluator(literate=YES)
#         self.assertTrue(literacy_evaluator.eligible)
#
#     def test_eligibility_literacy1(self):
#         """Assert illerate, no guardian is not eligible.
#         """
#         literacy_evaluator = LiteracyEvaluator(
#             literate=NO, guardian=NO)
#         self.assertFalse(literacy_evaluator.eligible)
#         self.assertTrue(literacy_evaluator.reason)
#
#     def test_eligibility_literacy2(self):
#         """Assert illerate, no guardian is not eligible.
#         """
#         literacy_evaluator = LiteracyEvaluator(
#             literate=NO, guardian=None)
#         self.assertFalse(literacy_evaluator.eligible)
#         self.assertTrue(literacy_evaluator.reason)
#
#     def test_eligibility_literacy3(self):
#         """ Assert literate with guardian is eligible.
#         """
#         literacy_evaluator = LiteracyEvaluator(
#             literate=NO, guardian=YES)
#         self.assertTrue(literacy_evaluator.eligible)
#
#     def test_hiv_status_evaluator(self):
#         """ Assert hiv status POS is eligible.
#         """
#         hiv_status_evaluator = HivStatusEvaluator(hiv_status=POS)
#         self.assertTrue(hiv_status_evaluator.eligible)
#
#     def test_hiv_status_evaluator2(self):
#         """ Assert hiv status POS is eligible.
#         """
#         hiv_status_evaluator = HivStatusEvaluator(hiv_status=NEG)
#         self.assertFalse(hiv_status_evaluator.eligible)
#
#     def test_eligibility(self):
#         """ Assert within age range and literate is eligible.
#         """
#         obj = Eligibility(
#             age=25,
#             literate=YES,
#             guardian=None,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#
#     def test_eligibility_reason(self):
#         """ Assert within age range and literate is eligible.
#         """
#         obj = Eligibility(
#             age=25,
#             literate=YES,
#             guardian=None,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility1(self):
#         """ Assert within age range and literate is eligible.
#         """
#         obj = Eligibility(
#             age=18,
#             literate=YES,
#             guardian=None,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility2(self):
#         """ Assert within age range and not literate with guardian is eligible.
#         """
#         obj = Eligibility(
#             age=64,
#             literate=NO,
#             guardian=YES,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility3(self):
#         """ Assert not a citizen, legal married to a citizen and marriage
#             certificates available is eligible.
#         """
#         obj = Eligibility(
#             age=64,
#             literate=NO,
#             guardian=YES,
#             legal_marriage=YES,
#             marriage_certificate=YES,
#             citizen=NO,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility_not_eligible_age(self):
#         """ Assert less than age range is not eligible.
#         """
#         obj = Eligibility(
#             age=15,
#             literate=YES,
#             guardian=None,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertFalse(obj.eligible)
#         self.assertIn('age<18', obj.reasons[0])
#
#     def test_eligibility_not_eligible_age2(self):
#         """ Assert less than age range is not eligible.
#         """
#         obj = Eligibility(
#             age=66,
#             literate=YES,
#             guardian=None,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertFalse(obj.eligible)
#         self.assertIn('age>64', obj.reasons[0])
#
#     def test_eligibility_not_eligible_age3(self):
#         """ Assert less than age range is not eligible.
#         """
#         obj = Eligibility(
#             age=16,
#             literate=YES,
#             guardian=NO,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertFalse(obj.eligible)
#         self.assertIn('Minor of age: 16 with no guardian.', obj.reasons[0])
#
#     def test_eligibility_not_eligible1s(self):
#         """ Assert illiterate and no guardian is not eligible.
#         """
#         obj = Eligibility(
#             age=16,
#             literate=NO,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertFalse(obj.eligible)
#         self.assertIn('Illiterate', obj.reasons[0])
#
#     def test_eligibility_hiv_status(self):
#         """ Assert hiv status POS is eligible.
#         """
#         obj = Eligibility(
#             age=64,
#             literate=NO,
#             guardian=YES,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility_hiv_status2(self):
#         """ Assert hiv status not POS is not eligible.
#         """
#         hiv_status_values = [NEG, IND, UNK, 'not_answering']
#         for hiv_status in hiv_status_values:
#             obj = Eligibility(
#                 age=64,
#                 literate=NO,
#                 guardian=YES,
#                 legal_marriage=NO,
#                 marriage_certificate=NO,
#                 citizen=YES,
#                 hiv_status=hiv_status,
#                 participation=ABLE_TO_PARTICIPATE)
#             self.assertFalse(obj.eligible)
#         self.assertIn('Not a positive participant', obj.reasons[0])
#
#     def test_eligibility_participation_reason(self):
#         """ Assert participation eligibility reason is None if able to
#         participate.
#         """
#         obj = Eligibility(
#             age=64,
#             literate=NO,
#             guardian=YES,
#             legal_marriage=NO,
#             marriage_certificate=NO,
#             citizen=YES,
#             hiv_status=POS,
#             participation=ABLE_TO_PARTICIPATE)
#         self.assertTrue(obj.eligible)
#         self.assertEqual(obj.reasons, [])
#
#     def test_eligibility_participation_reason2(self):
#         """ Assert participation eligibility reason is None if able to
#         participate.
#         """
#         optinos = [MENTAL_INCAPACITY, 'Deaf/Mute',
#                    'Too sick', 'Incarcerated', OTHER, NOT_APPLICABLE]
#         for participation in optinos:
#             obj = Eligibility(
#                 age=64,
#                 literate=NO,
#                 guardian=YES,
#                 legal_marriage=NO,
#                 marriage_certificate=NO,
#                 citizen=YES,
#                 hiv_status=POS,
#                 participation=participation)
#             self.assertFalse(obj.eligible)
#         self.assertIn(f'Not able participant {participation}', obj.reasons[0])
