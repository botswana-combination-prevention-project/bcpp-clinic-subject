from .modelform_mixin import SubjectModelFormMixin

from ..models import EnrollmentLoss


class EnrollmentLossForm(SubjectModelFormMixin):

    class Meta:
        model = EnrollmentLoss
        fields = '__all__'
