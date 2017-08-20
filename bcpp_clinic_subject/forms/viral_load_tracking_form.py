from bcpp_clinic_validators import ViralLoadTrackingFormValidator

from ..models import ViralLoadTracking
from .modelform_mixin import SubjectModelFormMixin


class ViralLoadTrackingForm (SubjectModelFormMixin):

    form_validator = ViralLoadTrackingFormValidator

    class Meta:
        model = ViralLoadTracking
        fields = '__all__'
