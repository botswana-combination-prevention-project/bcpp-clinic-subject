from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_protocol.validators import datetime_not_before_study_start

from .base_model_mixin import BaseModelMixin


class CrfModelMixin(BaseModelMixin, UpdatesCrfMetadataModelMixin, BaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`SubjectVisit`).
    """
    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_future, datetime_not_before_study_start],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    def get_search_slug_fields(self):
        fields = ['subject_identifier']
        return fields

    class Meta(BaseModelMixin.Meta):
        abstract = True
