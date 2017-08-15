from bcpp_clinic_validators import SubjectEligibilityFormValidator

from ..models import SubjectEligibility
from .modelform_mixin import SubjectModelFormMixin


class SubjectEligibilityForm(SubjectModelFormMixin):

    form_validator_cls = SubjectEligibilityFormValidator

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
