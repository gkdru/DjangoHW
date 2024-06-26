from django.urls import path

from . import views

app_name = "school"
urlpatterns = [
    path("task-1.1/", views.get_id, name="task-1.1"),
    path("task-1.2/", views.get_sum, name="task-1.2"),
]
