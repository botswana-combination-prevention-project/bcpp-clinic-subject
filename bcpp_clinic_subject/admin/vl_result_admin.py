from django.contrib import admin

from ..forms import VlResultForm
from ..models import VlResult
from ..admin_site import clinic_subject_admin
from ..admin import CrfModelAdminMixin


@admin.register(VlResult, site=clinic_subject_admin)
class ClinicVlResultAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = VlResultForm
    fields = (
        'clinic_visit',
        'report_datetime',
        'site',
        'clinician_initials',
        'collection_datetime',
        'assay_date',
        'result_value',
        'comment',
        'validation_date',
        'validated_by')

    list_display = ('clinic_visit', 'clinician_initials',
                    'collection_datetime', 'result_value', 'validated_by')

    search_fields = (
        'clinic_visit__subject_identifier',
        'clinician_initials', 'result_value',)
