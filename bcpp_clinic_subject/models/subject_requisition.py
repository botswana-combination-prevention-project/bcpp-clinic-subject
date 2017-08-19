from django.db import models
from django.db.models.deletion import PROTECT
from django.apps import apps as django_apps
from edc_base.model_mixins import BaseUuidModel
from edc_map.site_mappers import site_mappers
from bcpp_clinic_labs.model_mixins import SubjectRequisitionModelMixin

from .subject_visit import SubjectVisit


class SubjectRequisition(SubjectRequisitionModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    def save(self, *args, **kwargs):
        self.study_site = site_mappers.current_map_code
        self.study_site_name = site_mappers.current_map_area
        self.protocol_number = django_apps.get_app_config(
            'edc_protocol').protocol_number
        super().save(*args, **kwargs)

    class Meta(SubjectRequisitionModelMixin.Meta):
        unique_together = [
            'subject_visit', 'panel_name']
