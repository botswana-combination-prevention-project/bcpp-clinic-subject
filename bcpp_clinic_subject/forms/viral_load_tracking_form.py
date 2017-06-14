from bcpp_clinic_validations.form_validators import ViralLoadTrackingFormValidator

from ..models import ViralLoadTracking
from .modelform_mixin import SubjectModelFormMixin


class ViralLoadTrackingForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = ViralLoadTrackingFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = ViralLoadTracking
        fields = '__all__'
