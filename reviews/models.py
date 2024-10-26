"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    """
    Restaurant model
    """

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the restaurant.
        """
        return self.name

    def average_rating(self):
        """
        Calculate and return the average rating for the restaurant.
        """
        return self.reviews.aggregate(Avg("rating"))["rating__avg"]

    class Meta:
        ordering = ["name"]


class Review(models.Model):
    """
    Model representing a review for a restaurant.
    """

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the review.
        """
        return f"{self.restaurant.name} - {self.rating} stars"

    class Meta:
        ordering = ["-created"]
