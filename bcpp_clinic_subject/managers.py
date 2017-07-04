from django.db import models


class SubjectConsentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier, screening_identifier):
        return self.get(
            subject_identifier=subject_identifier,
            screening_identifier=screening_identifier)


class DailyLogManager(models.Manager):

    def get_by_natural_key(self, report_date, hostname_created):
        return self.get(
            report_date=report_date, hostname_created=hostname_created)


class DisenrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name)


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name
        )
