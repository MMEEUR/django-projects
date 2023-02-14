from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'email')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Comment'}),
        }
