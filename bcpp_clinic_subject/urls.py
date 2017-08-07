from django.conf.urls import url

from .admin_site import bcpp_clinic_subject_admin

urlpatterns = [
    url(r'^admin/', bcpp_clinic_subject_admin.urls),
]
