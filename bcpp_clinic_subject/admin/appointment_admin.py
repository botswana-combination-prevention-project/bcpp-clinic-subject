from django.contrib import admin

from edc_appointment.admin import AppointmentAdmin

from ..admin_site import bcpp_clinic_subject_admin
from ..forms import AppointmentForm
from ..models import Appointment


@admin.register(Appointment, site=bcpp_clinic_subject_admin)
class AppointmentAdmin(AppointmentAdmin, admin.ModelAdmin):

    form = AppointmentForm
