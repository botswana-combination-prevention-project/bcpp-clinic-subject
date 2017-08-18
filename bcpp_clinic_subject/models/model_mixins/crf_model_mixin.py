from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_protocol.validators import datetime_not_before_study_start

from .base_model_mixin import BaseModelMixin
from edc_metadata.model_mixins.rules.metadata_rules_model_mixin import MetadataRulesModelMixin
from edc_metadata.rules.site import site_metadata_rules


class CrfModelMixin(BaseModelMixin, UpdatesCrfMetadataModelMixin, MetadataRulesModelMixin, BaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`SubjectVisit`).
    """
    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_future, datetime_not_before_study_start],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    def run_metadata_rules(self):
        """Runs the rule groups for this .

        Gets called in the signal.
        """
        for rule_group in site_metadata_rules.registry.get(self._meta.rulegroup_app_label, []):
            if rule_group._meta.source_model == self._meta.label_lower:
                rule_group.evaluate_rules(visit=self)

    def get_search_slug_fields(self):
        fields = ['subject_identifier']
        return fields

    class Meta(BaseModelMixin.Meta):
        abstract = True
        rulegroup_app_label = 'bcpp_clinic_metadata_rules'
