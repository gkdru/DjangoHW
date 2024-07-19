from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from django.http import HttpResponse
from django.urls import reverse_lazy
import logging


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
