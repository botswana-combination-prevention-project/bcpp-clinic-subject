from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import (
    DashboardViewMixin as EdcDashboardViewMixin, AppConfigViewMixin)

from ....models import SubjectConsent, SubjectOffstudy
from ....model_wrappers import (
    CrfModelWrapper, SubjectVisitModelWrapper, RequisitionModelWrapper,
    SubjectConsentModelWrapper)
from .base_dashboard_view import BaseDashboardView


class DashboardView(
        BaseDashboardView, EdcDashboardViewMixin,
        AppConfigViewMixin, EdcBaseViewMixin,
        TemplateView):

    app_config_name = 'bcpp_clinic_subject'
    navbar_item_selected = 'bcpp_clinic_subject'
    consent_model_wrapper_class = SubjectConsentModelWrapper
    consent_model = SubjectConsent
    crf_model_wrapper_cls = CrfModelWrapper
    requisition_model_wrapper_cls = RequisitionModelWrapper
    visit_model_wrapper_cls = SubjectVisitModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anonymous = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.apps import apps as django_apps
        bcpp_clinic_subject_dashboard_url_name = django_apps.get_app_config(
            'bcpp_clinic_subject').dashboard_url_name,
        try:
            subject_offstudy = SubjectOffstudy.objects.get(
                subject_identifier=self.subject_identifier)
        except SubjectOffstudy.DoesNotExist:
            subject_offstudy = None
        context.update(
            subject_offstudy=subject_offstudy,
            bcpp_clinic_subject_dashboard_url_name=bcpp_clinic_subject_dashboard_url_name)
        return context
