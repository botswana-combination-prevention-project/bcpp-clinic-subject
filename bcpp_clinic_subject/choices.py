from django.utils.translation import ugettext_lazy as _

from edc_constants.constants import NOT_APPLICABLE, POS, NEG, IND, UNK, DWTA, OTHER
from bcpp_community import communities

from .constants import ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY

ordered_communities = list(communities.values())
ordered_communities.sort(key=lambda x: x.code)

REGISTRATION_TYPES = (
    ('initiation', 'Initiation Visit'),
    ('masa_vl_scheduled', 'MASA Scheduled Viral Load Visit'),
    ('OTHER', 'Other NON-Viral Load Visit')
)

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology',
     _('Routine oncology clinic visit (i.e. planned chemo, follow-up)')),
    ('Ill oncology', _('Ill oncology clinic visit')),
    ('Patient called', _('Patient called to come for visit')),
    (OTHER, _('Other, specify:')),
)

COMMUNITIES = [(c.code, c.name) for c in ordered_communities]
COMMUNITY = tuple(
    [(NOT_APPLICABLE, _('Not Applicable'))] + list(COMMUNITIES))
COMMUNITIES_NAMES = [(c.name, c.name) for c in ordered_communities]
VERBAL_HIVRESULT_CHOICE = (
    (POS, _('HIV Positive')),
    (NEG, _('HIV Negative')),
    (IND, _('Indeterminate')),
    (UNK, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
    (NOT_APPLICABLE, _('Not applicable')),
)

INABILITY_TO_PARTICIPATE_REASON = (
    (ABLE_TO_PARTICIPATE, ('ABLE to participate')),
    (MENTAL_INCAPACITY, ('Mental Incapacity')),
    ('Deaf/Mute', ('Deaf/Mute')),
    ('Too sick', ('Too sick')),
    ('Incarcerated', ('Incarcerated')),
    (OTHER, ('Other, specify.')),
    (NOT_APPLICABLE, ('Not applicable')),
)
