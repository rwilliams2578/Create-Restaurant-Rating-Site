"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.urls import path
from .views import (
    HomeView,
    RestaurantDetailView,
    AddReviewView,
    ReviewDetailView,
    UpdateReviewView,
    DeleteReviewView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name="restaurant_detail"),
    path("restaurant/<int:restaurant_pk>/add_review/", AddReviewView.as_view(), name="add_review"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/<int:pk>/update/", UpdateReviewView.as_view(), name="update_review"),
    path("review/<int:pk>/delete/", DeleteReviewView.as_view(), name="delete_review"),
]
