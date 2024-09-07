from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
