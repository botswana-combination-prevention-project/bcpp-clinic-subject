from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_subject'
    listboard_template_name = 'bcpp_clinic_subject/listboard.html'
    dashboard_template_name = 'bcpp_clinic_subject/dashboard.html'
    base_template_name = 'bcpp_clinic/base.html'
    listboard_url_name = 'bcpp_clinic_subject:listboard_url'
    dashboard_url_name = 'bcpp_clinic_subject:dashboard_url'
    admin_site_name = 'bcpp_clinic_subject_admin'
    eligibility_age_adult_lower = 16
    eligibility_age_adult_upper = 64

    def ready(self):
        from .models.signals import subject_consent_on_post_save
