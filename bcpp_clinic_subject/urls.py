from django.conf.urls import url

from .admin_site import bcpp_clinic_subject_admin

app_name = 'bcpp_clinic_subject'

urlpatterns = [
    url(r'^admin/', bcpp_clinic_subject_admin.urls),
]
