from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import (
    ModelAdminInstitutionMixin, ModelAdminNextUrlRedirectMixin,
    ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
    ModelAdminNextUrlRedirectError)
from edc_consent.modeladmin_mixins import ModelAdminConsentMixin

from edc_base.modeladmin_mixins import (
    audit_fieldset_tuple, audit_fields)

from ..admin_site import bcpp_clinic_subject_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            options.update(subject_identifier=obj.subject_identifier)
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


@admin.register(SubjectConsent, site=bcpp_clinic_subject_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin,
                          ModelAdminMixin, admin.ModelAdmin):

    dashboard_type = 'clinic'
    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'htc_identifier',
                'lab_identifier',
                'pims_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'gender',
                'dob',
                'study_site',
                'guardian_name',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'is_incarcerated',
                'may_store_samples',
                'comment',
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_copy')}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', )

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "identity_type": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "is_incarcerated": admin.VERTICAL,
        "is_literate": admin.VERTICAL,
        "language": admin.VERTICAL,
        "may_store_samples": admin.VERTICAL,
        "study_questions": admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

    def view_on_site(self, obj):
        try:
            return reverse(
                'bcpp_clinic_subject:dashboard_url', kwargs=dict(
                    subject_identifier=obj.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)
