from edc_lab.forms import RequisitionFormMixin

from ..models import SubjectRequisition
from .model_form_mixin import SubjectModelFormMixin


class SubjectRequisitionForm(RequisitionFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
