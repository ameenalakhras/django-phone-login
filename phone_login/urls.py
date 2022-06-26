from django.urls import re_path as url

from .views import GenerateOTP, ValidateOTP

urlpatterns = [
    url(r'^generate/$', GenerateOTP.as_view(), name="generate"),
    url(r'^validate/$', ValidateOTP.as_view(), name="validate"),
]
