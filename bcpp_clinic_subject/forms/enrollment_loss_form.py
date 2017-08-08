from edc_base.modelform_mixins import CommonCleanModelFormMixin

from ..models import EnrollmentLoss


class EnrollmentLossForm(CommonCleanModelFormMixin):

    class Meta:
        model = EnrollmentLoss
        fields = '__all__'
