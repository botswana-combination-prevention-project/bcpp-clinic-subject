from django.apps import AppConfig as DjangoApponfig

from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_subject'
    listboard_template_name = 'bcpp_clinic_subject/listboard.html'
    dashboard_template_name = 'bcpp_clinic_subject/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'bcpp_clinic_subject:listboard_url'
    dashboard_url_name = 'bcpp_clinic_subject:dashboard_url'
    admin_site_name = 'bcpp_clinic_subject_admin'
    eligibility_age_adult_lower = 16
    eligibility_age_adult_upper = 64


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'bcpp_clinic_subject': ('subject_visit', 'bcpp_clinic_subject.subjectvisit')}
