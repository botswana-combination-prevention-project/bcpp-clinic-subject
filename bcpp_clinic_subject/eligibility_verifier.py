from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


class EligibilityDoesNotExist(Exception):
    pass


class EnrollmentCreator:
    """Create an enrollment if does not exist after consent is created.
    """
    enrollment_model = 'bcpp_clinic_subject.enrollment'

    def __init__(self, subject_identifier=None, is_eligible=None):
        enrollment_model_cls = django_apps.get_model(self.enrollment_model)
        try:
            enrollment_model_cls.objects.get(
                subject_identifier=subject_identifier,
                visit_schedule_name=enrollment_model_cls._meta.visit_schedule_name)
        except ObjectDoesNotExist:
            enrollment_model_cls.objects.create(
                subject_identifier=subject_identifier,
                consent_identifier=self.consent_identifier,
                is_eligible=is_eligible)


class EligibilityVerifier:

    eligibility_model = 'bcpp_clinic_screening.subjecteligibility'
    enrollment_creator_cls = EnrollmentCreator

    def __init__(self, created=None, screening_identifier=None, subject_identifier=None):
        if created:
            eligibility_model_cls = django_apps.get_model(
                self.eligibility_model)
            try:
                eligibility_obj = eligibility_model_cls.objects.get(
                    screening_identifier=screening_identifier)
            except ObjectDoesNotExist:
                raise EligibilityDoesNotExist(
                    "Consent can not exist without an eligibility.")
            else:
                eligibility_obj.subject_identifier = subject_identifier
                eligibility_obj.save()
            self.enrollment_creator_cls(eligibility_obj=eligibility_obj)
