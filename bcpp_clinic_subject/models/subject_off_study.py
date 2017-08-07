from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyModelManager


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    objects = OffstudyModelManager()

    history = HistoricalRecords()
