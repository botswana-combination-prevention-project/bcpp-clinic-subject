from bcpp_clinic_validators import SubjectVisitFormValidator

from ..models import SubjectVisit
from .modelform_mixin import SubjectModelFormMixin


class SubjectVisitForm (SubjectModelFormMixin):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
