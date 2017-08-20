from django.apps import AppConfig as DjangoApponfig
from django.conf import settings


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_subject'
    admin_site_name = 'bcpp_clinic_subject_admin'
    eligibility_age_adult_lower = 18
    eligibility_age_adult_upper = 64
    eligibility_age_minor_lower = 16
    eligibility_age_minor_upper = 17

    def ready(self):
        from .signals import subject_consent_on_post_save


if 'bcpp_clinic_subject' in settings.APP_NAME:

    from datetime import datetime
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from dateutil.tz import gettz
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.facility import Facility
    from edc_constants.constants import FAILED_ELIGIBILITY
    from edc_map.apps import AppConfig as BaseEdcMapAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap
    from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
    from edc_timepoint.timepoint import Timepoint
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
    from bcpp_community.apps import AppConfig as BaseBcppCommunityAppConfig
    from .constants import RESEARCH_BLOOD_DRAW

    class BcppCommunityAppConfig(BaseBcppCommunityAppConfig):
        mapper_model = 'bcpp_clinic_subject.subjecteligibility'

    class EdcMapAppConfig(BaseEdcMapAppConfig):
        verbose_name = 'BCPP Mappers'
        mapper_model = 'bcpp_clinic_screening.subjecteligibility'

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP066'
        protocol_number = '066'
        protocol_name = 'BCPP Clinic'
        protocol_title = 'Botswana Combination Prevention Project'
        subject_types = [
            SubjectType(
                'subject', 'Research Subject',
                Cap(
                    model_name='bcpp_clinic_subject.subjectconsent',
                    max_subjects=9999)),
        ]
        study_open_datetime = datetime(
            2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

        @property
        def site_name(self):
            return 'test_community'

        @property
        def site_code(self):
            return '01'

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'bcpp_clinic_subject.subjectvisit': 'reason'}
        create_on_reasons = [RESEARCH_BLOOD_DRAW, SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY]
        metadata_rules_enabled = True  # default

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'bcpp_clinic_subject': (
                'subject_visit', 'bcpp_clinic_subject.subjectvisit')}

    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = [
            Timepoint(
                model='bcpp_clinic_subject.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
            Timepoint(
                model='bcpp_clinic_subject.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
        ]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        app_label = 'bcpp_clinic_subject'
        default_appt_type = 'clinic'
        facilities = {
            'clinic': Facility(
                name='clinic', days=[MO, TU, WE, TH, FR, SA, SU],
                slots=[99999, 99999, 99999, 99999, 99999, 99999, 99999])}
