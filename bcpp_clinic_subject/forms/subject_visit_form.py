from edc_visit_tracking.form_mixins import VisitFormMixin

from ..models import SubjectVisit
from .modelform_mixin import SubjectModelFormMixin


class SubjectVisitForm (VisitFormMixin, SubjectModelFormMixin):

    def validate_reason_and_info_source(self):
        pass

    class Meta:
        model = SubjectVisit
        fields = '__all__'
