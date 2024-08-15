from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from django.http import HttpResponse
import logging
from django.views.generic import ListView, DetailView
from .models import User, UserActivity


logger = logging.getLogger("django")


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "dz/login.html"
    success_url = reverse_lazy("succes")

    def form_valid(self, form):
        response = super().form_valid(form)
        logger.info(f"User {self.request.user} logged in successfully.")
        return response


def succes(request):
    logger.info(
        f"Succes view accessed by {request.user} with method {request.method} at URL {request.get_full_path()}"
    )
    return HttpResponse("Login Succes")


class UserListView(ListView):
    model = User
    template_name = "dz/users_list.html"
    context_object_name = "users"


class UserDetailView(DetailView):
    model = User
    template_name = "dz/user_detail.html"
    context_object_name = "user"


class UserCreateView(CreateView):
    model = User
    template_name = "dz/user_form.html"
    fields = ["username", "email"]
    success_url = reverse_lazy("users_list")


class UserUpdateView(UpdateView):
    model = User
    template_name = "dz/user_form.html"
    fields = ["username", "email"]
    success_url = reverse_lazy("users_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "dz/user_confirm_delete.html"
    success_url = reverse_lazy("users_list")


class UserActivityListView(ListView):
    model = UserActivity
    template_name = "dz/user_activity_list.html"
    context_object_name = "activities"
    ordering = ["-timestamp"]
