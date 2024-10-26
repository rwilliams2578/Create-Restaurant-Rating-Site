"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024

"""

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignUpView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
