from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins import FormAsJSONModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_offstudy.model_mixins import OffstudyMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_search.model_mixins import SearchSlugModelMixin, SearchSlugManager
from edc_visit_tracking.managers import CrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..subject_visit import SubjectVisit


class Manager(CrfModelManager, SearchSlugManager):
    pass


class BaseModelMixin(VisitTrackingCrfModelMixin, OffstudyMixin,
                     RequiresConsentMixin, PreviousVisitModelMixin, SearchSlugModelMixin,
                     FormAsJSONModelMixin, ReferenceModelMixin):

    """ Base model for all scheduled models.
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    objects = Manager()

    history = HistoricalRecords()

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['bcpp_clinic_subject.subjectvisit']

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'bcpp_clinic_subject.subjectconsent'
        abstract = True
