from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'comment', 'rating', 'teacher']
        labels = {
            'rating': '',
            'teacher': '',
        }
        widgets = {
            'rating': forms.HiddenInput(),
            'teacher': forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Comment'}),
        }
