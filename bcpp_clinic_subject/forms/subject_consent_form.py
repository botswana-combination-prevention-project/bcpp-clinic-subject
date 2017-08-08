from django import forms

from edc_consent.modelform_mixins import ConsentModelFormMixin

from ..choices import COMMUNITIES
from ..models import SubjectConsent
from .modelform_mixin import SubjectModelFormMixin


class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin):

    subject_eligibility_model = 'bcpp_clinic_screening.subjecteligibility'

    def clean(self):
        cleaned_data = super().clean()
        self.validate_data_fields()
        return cleaned_data

    def validate_data_fields(self):
        screening_identifier = self.cleaned_data.get(
            'screening_identifier')
        first_name = self.cleaned_data.get('first_name')
        initials = self.cleaned_data.get('initials')

        try:
            subject_eligibility = SubjectEligibility.objects.get(
                screening_identifier=screening_identifier)
        except SubjectEligibility.DoesNotExist:
            raise forms.ValidationError(
                f'Please complete \'{SubjectEligibility._meta.verbose_name}\' first.')
        else:
            if subject_eligibility.first_name != first_name:
                raise forms.ValidationError({
                    'first_name': f'Does not match {SubjectEligibility._meta.verbose_name}'})
            if subject_eligibility.initials != initials:
                raise forms.ValidationError({
                    'initials': f'Does not match {SubjectEligibility._meta.verbose_name}'})

    study_site = forms.ChoiceField(
        label='Study site',
        choices=COMMUNITIES,
        help_text="",
        widget=forms.RadioSelect())

    class Meta:
        model = SubjectConsent
        fields = '__all__'
