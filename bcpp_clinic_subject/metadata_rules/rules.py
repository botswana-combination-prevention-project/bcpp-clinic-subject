from edc_constants.constants import NO, YES, OTHER
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf_rule import CrfRule
from edc_metadata.rules.decorators import register
from edc_metadata.rules.logic import Logic
from edc_metadata.rules.predicate import P
from edc_metadata.rules.requisition_rule import RequisitionRule
from edc_metadata.rules.rule_group import RuleGroup

from ..constants import INITIATION, MASA_VL_SCHEDULED


@register()
class SubjectVisitRuleGroup(RuleGroup):

    initiation = RequisitionRule(
        logic=Logic(
            predicate=P(
                'registration_type',
                func=lambda x: True if x in [INITIATION, OTHER] else False),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_subject_clinic.subjectrequisition',
        panels=['Clinic Viral Load'],)

    is_drawn = CrfRule(
        logic=Logic(
            predicate=P(
                'registration_type', 'eq', MASA_VL_SCHEDULED),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_subject_clinic.viralloadtracking')

    class Meta:
        app_label = 'bcpp_clinic'
        source_model = 'bcpp_clinic_subject.subjectvisit'


@register()
class ViralLoadTrackingRuleGroup(RuleGroup):

    is_drawn = CrfRule(
        logic=Logic(
            predicate=P('is_drawn', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_subject_clinic.clinicvlresult')

    initiation = RequisitionRule(
        logic=Logic(
            predicate=P('is_drawn', 'eq', NO),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_lab.clinicrequisition',
        panels=['Clinic Viral Load'],)

    class Meta:
        app_label = 'bcpp_clinic'
        source_model = 'bcpp_subject_clinic.viralloadtracking'
