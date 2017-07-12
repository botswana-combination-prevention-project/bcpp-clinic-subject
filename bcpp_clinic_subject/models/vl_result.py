from django_crypto_fields.fields import EncryptedCharField
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_fields import InitialsField

from .crf_model_mixin import CrfModelMixin
from ..choices import COMMUNITIES_NAMES


class VlResult(CrfModelMixin):

    sample_id = models.CharField(
        verbose_name='Aliquot Identifier',
        max_length=25,
        unique=True,
        help_text="Aliquot identifier",
        editable=False)

    study_site = models.CharField(
        max_length=25,
        choices=COMMUNITIES_NAMES)

    clinician_initials = InitialsField(
        verbose_name='Clinician initial',
        default='--',
    )

    collection_datetime = models.DateTimeField(
        verbose_name='The datetime sample was drawn',
        help_text='',
    )

    received_datetime = models.DateTimeField(
        verbose_name='The datetime sample was received',
        help_text='',
    )

    test_datetime = models.DateTimeField(
        verbose_name='Test datetime',
        help_text='',
    )

    assay_date = models.DateField(
        verbose_name='Assay date',
        help_text='',
    )

    result_value = models.IntegerField(
        verbose_name="Result Value",
        help_text=("copies/ml"),)

    comment = models.TextField(
        verbose_name="Comment",
        max_length=250,
        blank=True,
        null=True
    )

    validation_datetime = models.DateTimeField(
        verbose_name='Datetime result was reported',
        help_text='',
    )

    assay_performed_by = EncryptedCharField(
        max_length=35,
        verbose_name="Assay performed by",
    )

    validated_by = EncryptedCharField(
        max_length=35,
        verbose_name="Validated by",
    )

    validation_reference = models.CharField(
        verbose_name='Validation reference',
        max_length=25,
        unique=True,
        help_text="Validation reference",
    )

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Clinic VL Result"
        verbose_name_plural = "Clinic VL Result"
