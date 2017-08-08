from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bcpp_clinic_subject_admin
from ..forms import EnrollmentLossForm
from ..models import EnrollmentLoss
from .model_admin_mixin import ModelAdminMixin


@admin.register(EnrollmentLoss, site=bcpp_clinic_subject_admin)
class EnrollmentLossAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = EnrollmentLossForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_eligibility',
                'report_datetime',
                'reason')}),
        audit_fieldset_tuple)

    list_display = (
        'report_datetime', 'reason', 'user_created',
        'user_modified', 'hostname_created')

    list_filter = ('report_datetime', 'reason', 'user_created',
                   'user_modified', 'hostname_created')

    radio_fields = {}

    instructions = []
