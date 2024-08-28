from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name = "up"
urlpatterns = [
path('create', views.ProfilereateView.as_view(), name='p-createV'),
path('succes', views.succes, name='succes'),
]