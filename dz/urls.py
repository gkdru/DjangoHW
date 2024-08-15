from django.urls import path
from . import views
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserActivityListView,
)

app_name = "dz"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("succes/", views.succes, name="succes"),
    path("users/", UserListView.as_view(), name="users_list"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("user/add/", UserCreateView.as_view(), name="user_add"),
    path("user/<int:pk>/edit/", UserUpdateView.as_view(), name="user_edit"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("user/activity/", UserActivityListView.as_view(), name="user_activity_list"),
]
