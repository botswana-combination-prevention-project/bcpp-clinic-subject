from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch

from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import bcpp_clinic_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectRequisition
from ..models import SubjectVisit
from .model_admin_mixin import ModelAdminMixin
from edc_base.modeladmin_mixins import audit_fieldset_tuple
from edc_visit_schedule.admin import visit_schedule_fieldset_tuple,\
    visit_schedule_fields
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fields


@admin.register(SubjectVisit, site=bcpp_clinic_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = SubjectVisitForm

    requisition_model = SubjectRequisition

    dashboard_type = 'clinic'

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'comments']}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple)

    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        "info_source",
        'created',
        'user_created',
    )

    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_code',
    )

    search_fields = (
        'appointment__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj) + audit_fields
                + visit_schedule_fields)

    def view_on_site(self, obj):
        try:
            return reverse(
                'bcpp_clinic_subject:dashboard_url', kwargs=dict(
                    subject_identifier=obj.subject_identifier,
                    appointment=str(obj.appointment.id)))
        except NoReverseMatch as e:
            print(e)
            return super().view_on_site(obj)
