from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'BCPP Clinic Subject'
    site_header = 'BCPP Clinic Subject'
    index_title = 'BCPP Clinic Subject'
    site_url = '/bcpp_clinic_subject/list/'


bcpp_clinic_subject_admin = AdminSite(name='bcpp_clinic_subject_admin')
