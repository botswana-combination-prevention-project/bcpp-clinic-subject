# coding=utf-8

from dateutil.relativedelta import relativedelta

from faker import Faker
from model_mommy.recipe import Recipe

from edc_base.utils import get_utcnow

from .models import SubjectLocator, SubjectConsent


fake = Faker()

subjectlocator = Recipe(
    SubjectLocator,
    alt_contact_cell_number='72200111',
    has_alt_contact=None,
    alt_contact_name=None,
    alt_contact_rel=None,
    alt_contact_cell=None,
    other_alt_contact_cell='760000111',
    alt_contact_tel=None)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    study_site='40',
    consent_datetime=get_utcnow(),
    dob=(get_utcnow() - relativedelta(years=25)).date(),
    first_name='TEST',
    last_name='TEST',
    initials='TT',
    gender='M',
    identity='12315678',
    confirm_identity='12315678',
    identity_type='OMANG',
    is_dob_estimated='-',)
