from django import forms

from edc_constants.constants import YES

from ..models import Questionnaire
from .modelform_mixin import SubjectModelFormMixin


class QuestionnaireForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

    class Meta:
        model = Questionnaire
        fields = '__all__'
