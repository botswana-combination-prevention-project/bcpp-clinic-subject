from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from edc_lab.model_mixins.requisition import (
    RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin)
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyMixin
from edc_visit_tracking.managers import (
    CrfModelManager as VisitTrackingCrfModelManager)
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin, PreviousVisitModelMixin)

from edc_consent.model_mixins import RequiresConsentMixin

from .subject_visit import SubjectVisit


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisition(
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, OffstudyMixin,
        RequiresConsentMixin, PreviousVisitModelMixin,
        UpdatesRequisitionMetadataModelMixin, SearchSlugModelMixin,
        BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    objects = Manager()

    def get_slugs(self):
        return ([self.subject_visit.subject_identifier,
                 self.requisition_identifier,
                 self.human_readable_identifier,
                 self.panel_name,
                 self.panel_object.abbreviation,
                 self.identifier_prefix]
                + self.subject_visit.household_member.get_slugs())

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'clinic_subject.subjectconsent'
        app_label = 'bcpp_clinic'
