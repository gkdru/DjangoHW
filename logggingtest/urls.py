from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.info_view, name="info_view"),
    path("error/", views.error_view, name="error_view"),
    path("debug/", views.debug_view, name="debug_view"),
]
