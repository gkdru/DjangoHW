from django.urls import path
from . import views

app_name = "dz"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("succes/", views.succes, name="succes"),
]
