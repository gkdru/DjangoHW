from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path("pass/", views.send_reset_emails_view, name="send-pass"),
]
