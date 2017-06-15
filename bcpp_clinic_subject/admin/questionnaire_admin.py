from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple


from ..admin import CrfModelAdminMixin
from ..admin_site import bcpp_clinic_subject_admin
from ..forms import QuestionnaireForm
from ..models import Questionnaire


@admin.register(Questionnaire, site=bcpp_clinic_subject_admin)
class QuestionnaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = QuestionnaireForm

    radio_fields = {
        "registration_type": admin.VERTICAL,
        "know_hiv_status": admin.VERTICAL,
        "current_hiv_status": admin.VERTICAL,
        "arv_evidence": admin.VERTICAL,
        "on_arv": admin.VERTICAL,
        "knows_last_cd4": admin.VERTICAL,
    }
    list_display = (
        'subject_visit', 'registration_type', 'on_arv', 'cd4_count',
        'report_datetime')
    list_filter = ('on_arv', 'report_datetime')
    search_fields = ('on_arv',)

    fieldsets = (
        (None, {
            'fields': (
                "subject_visit",
                "report_datetime",
                "registration_type",
                "know_hiv_status",
                "current_hiv_status",
                "arv_evidence",
                "on_arv",
                "knows_last_cd4",
                "cd4_count",)}),
        audit_fieldset_tuple)
