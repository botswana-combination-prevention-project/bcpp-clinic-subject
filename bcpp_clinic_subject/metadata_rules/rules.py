from edc_constants.constants import OTHER, YES, NO
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf_rule import CrfRule
from edc_metadata.rules.decorators import register
from edc_metadata.rules.logic import Logic
from edc_metadata.rules.predicate import P, PF
from edc_metadata.rules.requisition_rule import RequisitionRule
from edc_metadata.rules.rule_group import RuleGroup

from ..constants import INITIATION, MASA_VL_SCHEDULED
from ..labs import panel_vl


def func_requires_venous(visit_instance, *args):
    return True


@register()
class QuestionnaireRuleGroup(RuleGroup):

    initiation = RequisitionRule(
        logic=Logic(
            predicate=PF(
                'registration_type',
                func=lambda x: True if x in [INITIATION, OTHER] else False),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_clinic_subject.subjectrequisition',
        target_panels=[panel_vl],)

    viralloadtracking = CrfRule(
        predicate=P('registration_type', 'eq', MASA_VL_SCHEDULED),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['bcpp_clinic_subject.viralloadtracking'])

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.questionnaire'


@register()
class ViralLoadTrackingRuleGroup(RuleGroup):

    is_drawn = CrfRule(
        predicate=P('is_drawn', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['bcpp_clinic_subject.vlresult'])

    not_drawn = RequisitionRule(
        logic=Logic(
            predicate=P('is_drawn', 'eq', NO),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_model='bcpp_clinic_subject.subjectrequisition',
        target_panels=[panel_vl])

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.viralloadtracking'
