"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Avg
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Restaurant, Review
from .forms import ReviewForm


class HomeView(ListView):
    """
    View for the home page, displaying a list of all restaurants.
    """

    model = Restaurant
    template_name = "home.html"
    context_object_name = "restaurants"

    def get_queryset(self):
        """
        Returns the queryset of restaurants, annotated with their average rating.
        """
        return Restaurant.objects.annotate(avg_rating=Avg("reviews__rating"))


class RestaurantDetailView(DetailView):
    """
    View for displaying details of a single restaurant, including all its reviews.
    """

    model = Restaurant
    template_name = "restaurant_detail.html"
    context_object_name = "restaurant"

    def get_context_data(self, **kwargs):
        """
        Add extra context data including reviews and average rating.
        """
        context = super().get_context_data(**kwargs)
        context["reviews"] = self.object.reviews.all().order_by("-created")
        context["average_rating"] = self.object.reviews.aggregate(Avg("rating"))["rating__avg"]
        return context


class AddReviewView(LoginRequiredMixin, CreateView):
    """
    View for adding a new review to a restaurant.
    """

    model = Review
    form_class = ReviewForm
    template_name = "add_review.html"

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        form.instance.restaurant = get_object_or_404(Restaurant, pk=self.kwargs["restaurant_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful form submission.
        """
        return reverse("restaurant_detail", kwargs={"pk": self.kwargs["restaurant_pk"]})

    def get_context_data(self, **kwargs):
        """
        Insert the restaurant into the context dict.
        """
        context = super().get_context_data(**kwargs)
        context["restaurant"] = get_object_or_404(Restaurant, pk=self.kwargs["restaurant_pk"])
        return context


class ReviewDetailView(DetailView):
    """
    View for displaying details of a single review.
    """

    model = Review
    template_name = "review_detail.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        """
        Add extra context data including the associated restaurant.
        """
        context = super().get_context_data(**kwargs)
        context["restaurant"] = self.object.restaurant
        return context


class UpdateReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating an existing review.
    """

    model = Review
    form_class = ReviewForm
    template_name = "update_review.html"

    def test_func(self):
        """
        Ensure that only the author of the review can update it.
        """
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        """
        Return the URL to redirect to after successful form submission.
        """
        return reverse("review_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        """
        Add extra context data including the associated restaurant.
        """
        context = super().get_context_data(**kwargs)
        context["restaurant"] = self.object.restaurant
        return context


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting an existing review.
    """

    model = Review
    template_name = "delete_review.html"

    def test_func(self):
        """
        Ensure that only the author of the review can delete it.
        """
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        """
        Return the URL to redirect to after successful deletion.
        """
        return reverse("restaurant_detail", kwargs={"pk": self.object.restaurant.pk})

    def get_context_data(self, **kwargs):
        """
        Add extra context data including the associated restaurant.
        """
        context = super().get_context_data(**kwargs)
        context["restaurant"] = self.object.restaurant
        return context
