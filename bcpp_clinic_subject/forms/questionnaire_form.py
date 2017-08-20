from bcpp_clinic_validators import QuestionnaireFormValidator

from ..models import Questionnaire
from .modelform_mixin import SubjectModelFormMixin


class QuestionnaireForm (SubjectModelFormMixin):

    form_validator_cls = QuestionnaireFormValidator

    class Meta:
        model = Questionnaire
        fields = '__all__'
