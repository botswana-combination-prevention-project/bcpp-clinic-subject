from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin
from bcpp_clinic_validators import SubjectEligibilityFormValidator
from ..models import SubjectEligibility


class SubjectEligibilityForm(FormValidatorMixin, CommonCleanModelFormMixin):

    form_validator_cls = SubjectEligibilityFormValidator

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
