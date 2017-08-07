from django.db import models
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_lab.model_mixins.requisition import RequisitionModelMixin, RequisitionStatusMixin
from edc_lab.model_mixins.requisition import RequisitionIdentifierMixin

from .base_model_mixin import BaseModelMixin


class RequisitionModelMixin(BaseModelMixin, RequisitionModelMixin, RequisitionStatusMixin,
                            RequisitionIdentifierMixin, UpdatesRequisitionMetadataModelMixin,
                            models.Model):

    """ Base model for all requiistion models.
    """

    def get_search_slug_fields(self):
        fields = [
            'requisition_identifier',
            'subject_identifier',
            'human_readable_identifier',
            'panel_name',
            'panel_object.abbreviation',
            'identifier_prefix']
        return fields

    class Meta(BaseModelMixin.Meta):
        abstract = True
