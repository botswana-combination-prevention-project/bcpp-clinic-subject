from ..models import DailyLog
from .modelform_mixin import SubjectModelFormMixin


class DailyLogForm(SubjectModelFormMixin):

    class Meta:
        model = DailyLog
        fields = '__all__'
