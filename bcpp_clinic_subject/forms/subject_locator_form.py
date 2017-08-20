from django import forms

from ..models import SubjectLocator
from .modelform_mixin import SubjectModelFormMixin


class SubjectLocatorForm (SubjectModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectLocator
        fields = '__all__'
