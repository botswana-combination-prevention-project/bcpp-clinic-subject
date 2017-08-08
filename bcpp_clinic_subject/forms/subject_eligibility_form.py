from edc_base.modelform_mixins import CommonCleanModelFormMixin

from ..models import SubjectEligibility


class SubjectEligibilityForm(CommonCleanModelFormMixin):

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
