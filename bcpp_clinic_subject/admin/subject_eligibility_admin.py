from django.contrib import admin
from edc_base.fieldsets import FieldsetsModelAdminMixin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bcpp_clinic_subject_admin
from ..forms import SubjectEligibilityForm
from ..models import SubjectEligibility
from .model_admin_mixin import ModelAdminMixin


@admin.register(SubjectEligibility, site=bcpp_clinic_subject_admin)
class SubjectEligibilityAdmin(
        ModelAdminMixin, FieldsetsModelAdminMixin, admin.ModelAdmin):

    form = SubjectEligibilityForm

    instructions = ['This form is a tool to assist the Interviewer to confirm the '
                    'Eligibility status of the subject. After entering the required items, click SAVE.']

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'first_name',
                'initials',
                'gender',
                'age_in_years',
                'has_identity',
                "citizen",
                "legal_marriage",
                "marriage_certificate",
                "part_time_resident",
                "literacy",
                "guardian",
                'inability_to_participate',
                "hiv_status",)}),
        audit_fieldset_tuple)

    list_display = (
        'report_datetime', 'gender', 'is_eligible', 'is_consented', 'is_refused', 'map_area')

    list_filter = ('gender', 'is_eligible', 'is_consented',
                   'is_refused', 'report_datetime', 'map_area')

    radio_fields = {
        'has_identity': admin.VERTICAL,
        "gender": admin.VERTICAL,
        "citizen": admin.VERTICAL,
        "legal_marriage": admin.VERTICAL,
        "marriage_certificate": admin.VERTICAL,
        "part_time_resident": admin.VERTICAL,
        "literacy": admin.VERTICAL,
        "guardian": admin.VERTICAL,
        "inability_to_participate": admin.VERTICAL,
        "hiv_status": admin.VERTICAL,
    }

    search_fields = (
        'first_name',
        'initials',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
