# from model_mommy import mommy
# from django.utils import timezone
# from edc_base.utils import get_utcnow
# from edc_constants.constants import YES, MALE, POS, NOT_APPLICABLE
# from edc_visit_tracking.constants import SCHEDULED
#
# from ..constants import ABLE_TO_PARTICIPATE
# from ..models import Appointment, SubjectEligibility, SubjectVisit
#
#
# class TestClinicMixin:
#
#     def complete_clinic_visit(self):
#         def make_eligibility():
#             options = dict(
#                 report_datetime=timezone.now(),
#                 part_time_resident=YES,
#                 initials='TT',
#                 gender=MALE,
#                 has_identity=YES,
#                 hiv_status=POS,
#                 inability_to_participate=ABLE_TO_PARTICIPATE,
#                 citizen=YES,
#                 literacy=YES,
#                 guardian=NOT_APPLICABLE,
#                 age_in_years=27)
#             eligibility = SubjectEligibility.objects.create(**options)
#             self.assertTrue(eligibility.is_eligible)
#             return eligibility
#         subject_consent = mommy.make_recipe(
#             'bcpp_clinic_subject.subjectconsent',
#             screening_identifier=make_eligibility().screening_identifier)
#         appointment = Appointment.objects.get(
#             subject_identifier=subject_consent.subject_identifier)
#         return SubjectVisit.objects.create(
#             report_datetime=get_utcnow(), appointment=appointment,
#             reason=SCHEDULED)
