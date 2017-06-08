from edc_consent.modelform_mixins import ConsentModelFormMixin

from ..models import SubjectConsent
from .modelform_mixin import SubjectModelFormMixin


class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectConsent
        fields = '__all__'
