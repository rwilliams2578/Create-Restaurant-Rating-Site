"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Restaurant, Review
from django.core.exceptions import ValidationError


class ModelTests(TestCase):
    def setUp(self):
        """
        Create Test user and Restaurant
        """
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_restaurant_creation(self):
        """
        Test creating Restaurant
        """
        self.assertEqual(self.restaurant.name, "Test Restaurant")

    def test_review_creation(self):
        """
        Test Review creation
        """
        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=4, comment="Great food!")
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, "Great food!")

    def test_review_rating_range(self):
        """
        Test Review rating range
        """
        with self.assertRaises(ValidationError):
            review = Review(restaurant=self.restaurant, user=self.user, rating=6, comment="Invalid rating")
            review.full_clean()


class ViewTests(TestCase):
    """
    Test views
    """

    def setUp(self):
        """
        Create test user and restaurant
        """
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_home_view(self):
        """
        Test home view
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")

    def test_restaurant_detail_view(self):
        """
        Test restaurant detail view
        """
        response = self.client.get(reverse("restaurant_detail", args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")

    def test_add_review_view(self):
        """
        Test add review view
        """
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("add_review", args=[self.restaurant.id]), {"rating": 4, "comment": "Great place!"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

    def test_update_review_view(self):
        """
        Test update review view
        """
        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=3, comment="Good")
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("update_review", args=[review.id]), {"rating": 5, "comment": "Excellent!"})
        self.assertEqual(response.status_code, 302)
        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.rating, 5)
        self.assertEqual(updated_review.comment, "Excellent!")

    def test_delete_review_view(self):
        """
        Test delete review view
        """
        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=3, comment="Good")
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("delete_review", args=[review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 0)


class AuthenticationTests(TestCase):
    """
    Test authentication
    """

    def setUp(self):
        """
        Set up authentication client
        """
        self.client = Client()
        self.signup_url = reverse("signup")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

    def test_signup_view(self):
        """
        Test signup view
        """
        response = self.client.post(
            self.signup_url, {"username": "newuser", "password1": "testpassword123", "password2": "testpassword123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        """
        Test login view
        """
        User.objects.create_user(username="testuser", password="12345")
        response = self.client.post(self.login_url, {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_logout_view(self):
        """
        Test logout view
        """
        User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse("_auth_user_id" in self.client.session)


class FormTests(TestCase):
    """
    Test forms

    """

    def setUp(self):
        """
        Set up test user and restaurant
        """
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_review_form_valid_data(self):
        """
        Test review form data
        """
        form_data = {"rating": 4, "comment": "Great food!"}
        response = self.client.post(reverse("add_review", args=[self.restaurant.id]), form_data)
        self.assertEqual(response.status_code, 302)
