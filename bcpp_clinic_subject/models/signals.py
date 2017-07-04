from django.db.models.signals import post_save
from django.dispatch import receiver

from bcpp_clinic_screening.exceptions import ElibilityError
from bcpp_clinic_screening.models import SubjectEligibility

from .subject_consent import SubjectConsent


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Updates subject eligibility's subject identifier for this subject consent.
    """
    subject_eligibility = None
    if not raw:
        if created:
            try:
                subject_eligibility = SubjectEligibility.objects.get(
                    screening_identifier=instance.screening_identifier)
            except SubjectEligibility.DoesNotExist:
                raise ElibilityError(
                    "Consent can not exist without an eligibility.")
            else:
                subject_eligibility.subject_identifier = instance.subject_identifier
                subject_eligibility.save()
            instance.update_or_create_enrollment(subject_eligibility)
