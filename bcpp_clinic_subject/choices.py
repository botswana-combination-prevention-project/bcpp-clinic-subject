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


COMMUNITIES = (
    (1, 'test_community'),
    (17, 'bokaa'),
    (12, 'digawana'),
    (35, 'gumare'),
    (34, 'gweta'),
    (16, 'lentsweletau'),
    (21, 'lerala'),
    (15, 'letlhakeng'),
    (37, 'masunga'),
    (31, 'mathangwane'),
    (23, 'maunatlala'),
    (29, 'metsimotlhabe'),
    (26, 'mmadinare'),
    (32, 'mmandunyane'),
    (19, 'mmankgodi'),
    (20, 'mmathethe'),
    (13, 'molapowabojang'),
    (38, 'nata'),
    (27, 'nkange'),
    (18, 'oodi'),
    (14, 'otse'),
    (33, 'rakops'),
    (24, 'ramokgonami'),
    (11, 'ranaka'),
    (28, 'sebina'),
    (39, 'sefhare'),
    (22, 'sefophe'),
    (36, 'shakawe'),
    (25, 'shoshong'),
    (30, 'tati_siding'),
    (40, 'tsetsebjwe'))
