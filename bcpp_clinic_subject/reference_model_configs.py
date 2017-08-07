from edc_reference.site import ReferenceModelConfig
from edc_reference.site import site_reference_configs


reference = ReferenceModelConfig(
    model='bcpp_clinic_subject.questionnaire',
    fields=['registration_type'])
site_reference_configs.register(reference)

reference = ReferenceModelConfig(
    model='bcpp_clinic_subject.viralloadtracking',
    fields=['is_drawn'])
site_reference_configs.register(reference)

reference = ReferenceModelConfig(
    model='bcpp_clinic_subject.vlresult',
    fields=['report_datetime'])
site_reference_configs.register(reference)
#
reference = ReferenceModelConfig(
    model='bcpp_clinic_subject.subjectrequisition',
    fields=['report_datetime'])
site_reference_configs.register(reference)
