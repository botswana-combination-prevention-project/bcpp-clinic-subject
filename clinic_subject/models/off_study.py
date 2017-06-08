from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyModelManager


class OffStudy(OffstudyModelMixin, BaseUuidModel):

    objects = OffstudyModelManager()

    history = HistoricalRecords()

    class Meta:
        app_label = "clinic_subject"
        verbose_name = "Clinic Off Study"
        verbose_name_plural = "Clinic Off Study"
