from django.apps import apps as django_apps
from edc_base.model_mixins import BaseUuidModel
from edc_map.site_mappers import site_mappers

from .model_mixins import RequisitionModelMixin


class SubjectRequisition(RequisitionModelMixin, BaseUuidModel):

    def save(self, *args, **kwargs):
        self.study_site = site_mappers.current_map_code
        self.study_site_name = site_mappers.current_map_area
        self.protocol_number = django_apps.get_app_config(
            'edc_protocol').protocol_number
        super().save(*args, **kwargs)
