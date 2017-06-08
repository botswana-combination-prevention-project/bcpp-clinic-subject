from edc_visit_tracking.form_mixins import VisitFormMixin

from ..models import SubjectVisit
from .model_form_mixin import SubjectModelFormMixin


class SubjectVisitForm (VisitFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectVisit
        fields = '__all__'
