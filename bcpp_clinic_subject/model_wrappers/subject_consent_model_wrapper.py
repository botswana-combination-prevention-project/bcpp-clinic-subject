from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper
from bcpp_clinic_screening.models.subject_eligibility import SubjectEligibility
from edc_consent.exceptions import ConsentError


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'bcpp_clinic_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'bcpp_clinic_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier', ]
    querystring_attrs = [
        'gender', 'screening_identifier', 'first_name', 'initials', 'modified']

    @property
    def map_area(self):
        try:
            subject_eligibility = SubjectEligibility.objects.get()
        except SubjectEligibility.DoesNotExist:
            raise ConsentError(
                'Missing subject eligibility with identifier '
                f'{subject_eligibility.screening_identifier}.')
        else:
            return subject_eligibility.map_area
