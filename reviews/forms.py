"""
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024
"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating or updating a review.
    """

    class Meta:
        model = Review
        fields = ["rating", "body"]
        widgets = {
            "rating": forms.Select(choices=[(i, i) for i in range(1, 6)]),
            "body": forms.Textarea(attrs={"rows": 4}),
        }
