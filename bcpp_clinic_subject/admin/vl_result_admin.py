from django.contrib import admin

from ..forms import VlResultForm
from ..models import VlResult
from ..admin_site import bcpp_clinic_subject_admin
from ..admin import CrfModelAdminMixin


@admin.register(VlResult, site=bcpp_clinic_subject_admin)
class VlResultAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = VlResultForm
    fields = (
        'subject_visit',
        'report_datetime',
        'study_site',
        'clinician_initials',
        'collection_datetime',
        'test_datetime',
        'assay_date',
        'result_value',
        'received_datetime',
        'comment',
        'validation_datetime',
        'validated_by')

    list_display = ('subject_visit', 'clinician_initials',
                    'collection_datetime', 'result_value', 'validated_by')

    search_fields = (
        'subject_visit__subject_identifier',
        'clinician_initials', 'result_value',)
