from django.apps import apps as django_apps
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


@receiver(post_save, weak=False, dispatch_uid="crf_metadata_update_on_post_save")
def crf_metadata_update_on_post_save(sender, instance, raw, created, using,
                                     update_fields, **kwargs):
    """Update the meta data record on post save of a model.
    """

    if not raw:
        try:
            instance.metadata_update()
            if django_apps.get_app_config('edc_metadata').metadata_rules_enabled:
                instance.run_metadata_rules()
        except AttributeError as e:
            if 'metadata_update' not in str(e):
                raise AttributeError(e) from e
