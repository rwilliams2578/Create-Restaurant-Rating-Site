"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("reviews.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    # path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
