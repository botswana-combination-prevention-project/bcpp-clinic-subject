from django.core.management.color import color_style

from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..visit_schedule import schedule


style = color_style()


visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='BCPP Clinic Survey',
    app_label='bcpp_clinic_subject',
    visit_model='bcpp_clinic_subject.subjectvisit',
    offstudy_model='bcpp_clinic_subject.subjectoffstudy',
    previous_visit_schedule=None,
)

visit_schedule.add_schedule(schedule)

site_visit_schedules.register(visit_schedule)
