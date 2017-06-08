from django import forms

from edc_base.modelform_mixins import JSONModelFormMixin
from edc_base.modelform_mixins import CommonCleanModelFormMixin

from ..models import SubjectVisit


class SubjectModelFormMixin(CommonCleanModelFormMixin,
                            OtherSpecifyValidationMixin,
                            ApplicableValidationMixin,
                            Many2ManyModelValidationMixin,
                            RequiredFieldValidationMixin,
                            JSONModelFormMixin,
                            forms.ModelForm):

    visit_model = SubjectVisit
