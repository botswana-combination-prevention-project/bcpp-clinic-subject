from bcpp_clinic_validations.form_validations import QuestionnaireFormValidator

from ..models import Questionnaire
from .modelform_mixin import SubjectModelFormMixin


class QuestionnaireForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = QuestionnaireFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Questionnaire
        fields = '__all__'
