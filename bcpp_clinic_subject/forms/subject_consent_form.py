from django import forms

from edc_consent.modelform_mixins import ConsentModelFormMixin

from ..choices import COMMUNITIES
from ..models import SubjectConsent
from .modelform_mixin import SubjectModelFormMixin


class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=COMMUNITIES,
        help_text="",
        widget=forms.RadioSelect())

    class Meta:
        model = SubjectConsent
        fields = '__all__'
