# coding=utf-8

from dateutil.relativedelta import relativedelta

from faker import Faker
from model_mommy.recipe import Recipe

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO

from .models import (
    SubjectLocator, SubjectConsent, Questionnaire, ViralLoadTracking)

from .constants import MASA_VL_SCHEDULED

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

questionnaire = Recipe(
    Questionnaire,
    registration_type=MASA_VL_SCHEDULED,
    on_arv=YES,
    knows_last_cd4=NO)

viralloadtracking = Recipe(
    ViralLoadTracking,
    clinician_initials='TT',
    drawn_datetime=get_utcnow(),
    is_drawn=YES)
