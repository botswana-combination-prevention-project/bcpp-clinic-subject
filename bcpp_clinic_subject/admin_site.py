from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'BCPP Clinic Subject'
    site_header = 'BCPP Clinic Subject'
    index_title = 'BCPP Clinic Subject'
    site_url = '/clinic_subject/list/'


clinic_subject_admin = AdminSite(name='clinic_subject_admin')
