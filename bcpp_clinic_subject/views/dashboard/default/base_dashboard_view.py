from edc_dashboard.view_mixins import (
    ShowHideViewMixin, SubjectIdentifierViewMixin,
    MetaDataViewMixin, ConsentViewMixin)

from ..appointment_view_mixin import AppointmentViewMixin
from ..subject_visit_view_mixin import SubjectVisitViewMixin
from ..visit_schedule_view_mixin import VisitScheduleViewMixin
from .subject_locator_view_mixin import SubjectLocatorViewMixin


class BaseDashboardView(
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectLocatorViewMixin,
        SubjectVisitViewMixin,
        AppointmentViewMixin,
        VisitScheduleViewMixin,
        ShowHideViewMixin,
        SubjectIdentifierViewMixin):
    pass
