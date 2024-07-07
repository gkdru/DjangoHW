from django.urls import path, re_path
from . import views

app_name = "tasks"
urlpatterns = [
    path("all", views.get_all, name="all"),  # вытаскиеваем все task'и
    re_path(
        r"^create/$", views.createTask.as_view(), name="createTask"
    ),  # создаем task
    re_path(
        "delete/(?P<pk>\d+)/", views.deleteTaks.as_view(), name="deleteTask"
    ),  # удаляем его
]
