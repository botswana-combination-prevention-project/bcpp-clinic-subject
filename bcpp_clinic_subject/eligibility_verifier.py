from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


class EligibilityDoesNotExist(Exception):
    pass


class ConsentDoesNotExist(Exception):
    pass


class EnrollmentCreator:
    """Create an enrollment if does not exist.
    """
    enrollment_model = 'bcpp_clinic_subject.enrollment'

    def __init__(self, subject_identifier=None, is_eligible=None):
        enrollment_model_cls = django_apps.get_model(self.enrollment_model)
        SubjectConsent = django_apps.get_model(
            'bcpp_clinic_subject.subjectconsent')
        try:
            subject_consent = SubjectConsent.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            raise ConsentDoesNotExist(
                f'Subject consent should exist for subject {subject_identifier}')
        try:
            enrollment_model_cls.objects.get(
                subject_identifier=subject_identifier,
                visit_schedule_name=enrollment_model_cls._meta.visit_schedule_name)
        except ObjectDoesNotExist:
            enrollment_model_cls.objects.create(
                subject_identifier=subject_identifier,
                consent_identifier=subject_consent.consent_identifier,
                is_eligible=is_eligible)


class EligibilityVerifier:

    eligibility_model = 'bcpp_clinic_subject.subjecteligibility'
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
                    "Eligibility must be completed first.")
            else:
                eligibility_obj.subject_identifier = subject_identifier
                eligibility_obj.save()
            self.enrollment_creator_cls(
                subject_identifier=subject_identifier,
                is_eligible=eligibility_obj.is_eligible)
