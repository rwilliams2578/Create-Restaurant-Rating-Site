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
    """Test model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_restaurant_creation(self):
        """Test restaurant creation"""

        self.assertEqual(self.restaurant.name, "Test Restaurant")

    def test_review_creation(self):
        """Test review creation"""

        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=4, body="Great food!")
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.body, "Great food!")

    def test_review_rating_range(self):
        """Test review rating range"""

        with self.assertRaises(ValidationError):
            review = Review(restaurant=self.restaurant, user=self.user, rating=6, body="Invalid rating")
            review.full_clean()


class ViewTests(TestCase):
    """Test View"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_home_view(self):
        """Test home view"""

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")

    def test_restaurant_detail_view(self):
        """Test restaurant detail"""

        response = self.client.get(reverse("restaurant_detail", args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")

    def test_add_review_view(self):
        """Test add review"""

        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("add_review", args=[self.restaurant.id]), {"rating": 4, "body": "Great place!"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

    def test_update_review_view(self):
        """Test review view"""

        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=3, body="Good")
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("update_review", args=[review.id]), {"rating": 5, "body": "Excellent!"})
        self.assertEqual(response.status_code, 302)
        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.rating, 5)
        self.assertEqual(updated_review.body, "Excellent!")

    def test_delete_review_view(self):
        """Test delete view"""

        review = Review.objects.create(restaurant=self.restaurant, user=self.user, rating=3, body="Good")
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("delete_review", args=[review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 0)


class AuthenticationTests(TestCase):
    """Test authentication"""

    def test_signup_view(self):
        response = self.client.post(
            reverse("signup"), {"username": "newuser", "password1": "testpassword123", "password2": "testpassword123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        """Test login view"""

        User.objects.create_user(username="testuser", password="12345")
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_logout_view(self):
        """Test logout view"""

        User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertFalse("_auth_user_id" in self.client.session)


class FormTests(TestCase):
    """Test form"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_review_form_valid_data(self):
        """Test review form data"""

        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("add_review", args=[self.restaurant.id]), {"rating": 4, "body": "Great food!"}
        )
        self.assertEqual(response.status_code, 302)

    def test_review_form_invalid_data(self):
        """Test review form data"""

        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("add_review", args=[self.restaurant.id]), {"rating": 6, "body": "Invalid rating"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Review.objects.exists())
