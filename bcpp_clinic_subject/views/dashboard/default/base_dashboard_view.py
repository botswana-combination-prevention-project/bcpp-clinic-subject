from edc_dashboard.view_mixins import (
    ShowHideViewMixin, SubjectIdentifierViewMixin,
    MetaDataViewMixin, ConsentViewMixin)

from ..appointment_view_mixin import AppointmentViewMixin
from ..subject_visit_view_mixin import SubjectVisitViewMixin
from ..visit_schedule_view_mixin import VisitScheduleViewMixin


class BaseDashboardView(
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectVisitViewMixin,
        AppointmentViewMixin,
        VisitScheduleViewMixin,
        ShowHideViewMixin,
        SubjectIdentifierViewMixin):
    pass
