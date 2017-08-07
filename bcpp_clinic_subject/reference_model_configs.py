from edc_reference import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'bcpp_clinic_subject.questionnaire': ['registration_type'],
    'bcpp_clinic_subject.viralloadtracking': ['is_drawn']}

for model, fields in configs.items():
    site_reference_configs.add_fields_to_config(model, fields)
