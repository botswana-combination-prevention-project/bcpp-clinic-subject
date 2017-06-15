from bcpp_clinic_validations.form_validators import SubjectLocatorFormValidator

from ..models import SubjectLocator
from .modelform_mixin import SubjectModelFormMixin


class SubjectLocatorForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SubjectLocatorFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = SubjectLocator
        fields = '__all__'
