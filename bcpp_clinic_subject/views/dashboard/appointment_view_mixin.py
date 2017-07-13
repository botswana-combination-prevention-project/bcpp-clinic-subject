from edc_appointment.models import Appointment
from edc_appointment.view_mixins.appointment_view_mixin import (
    AppointmentViewMixin as BaseAppointmentMixin)

from ...model_wrappers import AppointmentModelWrapper


class AppointmentViewMixin(BaseAppointmentMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper

    @property
    def appointments(self):
        appointments = super().appointments
        return [obj for obj in appointments if obj.subject_identifier == self.subject_identifier]

    def empty_appointment(self, **kwargs):
        return Appointment()
