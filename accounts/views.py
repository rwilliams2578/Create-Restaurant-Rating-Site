"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024

"""

from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    """
    View for handling user login.
    """

    template_name = "registration/login.html"
    success_url = reverse_lazy("home")


class CustomLogoutView(LogoutView):
    """
    View for handling user logout.
    """

    next_page = "home"


class SignUpView(CreateView):
    """
    View for handling user registration.
    """

    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
