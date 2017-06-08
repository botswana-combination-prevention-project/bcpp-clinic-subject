from django.utils.translation import ugettext_lazy as _

from edc_constants.constants import OTHER


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
