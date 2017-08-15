from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import SubjectConsent
from .eligibility_verifier import EligibilityVerifier


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Updates subject eligibility's subject identifier for this subject consent.
    """
    if not raw:
        EligibilityVerifier(
            created=instance.id,
            subject_identifier=instance.subject_identifier,
            screening_identifier=instance.screening_identifier)
