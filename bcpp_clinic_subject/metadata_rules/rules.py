from edc_constants.constants import OTHER, YES, NO
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule, RequisitionRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P, PF
from edc_metadata.rules.requisition import RequisitionRuleGroup

from ..constants import INITIATION, MASA_VL_SCHEDULED
from ..labs import panel_vl


@register()
class QuestionnaireCrfRuleGroup(CrfRuleGroup):

    viralloadtracking = CrfRule(
        predicate=P('registration_type', 'eq', MASA_VL_SCHEDULED),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['viralloadtracking'])

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.questionnaire'


@register()
class QuestionnaireRequisitionRuleGroup(RequisitionRuleGroup):

    initiation = RequisitionRule(
        predicate=PF(
            'registration_type',
            func=lambda x: True if x in [INITIATION, OTHER] else False),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[panel_vl],)

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.questionnaire'
        requisition_model = 'subjectrequisition'


@register()
class ViralLoadTrackingRequisitionRuleGroup(RequisitionRuleGroup):

    not_drawn = RequisitionRule(
        predicate=P('is_drawn', 'eq', NO),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[panel_vl])

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.viralloadtracking'
        requisition_model = 'subjectrequisition'


@register()
class ViralLoadTrackingCrfRuleGroup(CrfRuleGroup):

    is_drawn = CrfRule(
        predicate=P('is_drawn', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['vlresult'])

    class Meta:
        app_label = 'bcpp_clinic_subject'
        source_model = 'bcpp_clinic_subject.viralloadtracking'
