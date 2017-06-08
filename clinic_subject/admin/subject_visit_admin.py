from django.contrib import admin


from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import bcpp_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectRequisition
from ..models import SubjectVisit


@admin.register(SubjectVisit, site=bcpp_subject_admin)
class ClinicVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = SubjectVisitForm

    requisition_model = SubjectRequisition

    dashboard_type = 'clinic'

    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        "info_source",
        'created',
        'user_created',
    )

    fieldsets = ()

    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_code',
    )

    search_fields = (
        'appointment__subject_identifier',
    )
