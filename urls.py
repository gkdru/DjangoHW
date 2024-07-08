from django.urls import path

from . import views

app_name = "dz"
urlpatterns = [path("all", views.get_title, name="get_all")]
