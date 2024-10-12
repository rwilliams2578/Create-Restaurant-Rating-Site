"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.contrib import admin
from .models import Restaurant, Review


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """
    Restaurant admin
    """

    list_display = ("name", "created", "updated")
    search_fields = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review admin
    """

    list_display = ("restaurant", "user", "rating", "created")
    list_filter = ("restaurant", "rating")
    search_fields = ("restaurant__name", "user__username")
