"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AccountTests(TestCase):
    def test_signup_view(self):
        """
        Test user registration functionality.
        """
        response = self.client.post(
            reverse("accounts:signup"),
            {"username": "newuser", "password1": "testpassword123", "password2": "testpassword123"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        """
        Test user login functionality.
        """
        User.objects.create_user(username="testuser", password="12345")
        response = self.client.post(reverse("accounts:login"), {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_logout_view(self):
        """
        Test user logout functionality.
        """
        User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertFalse("_auth_user_id" in self.client.session)
