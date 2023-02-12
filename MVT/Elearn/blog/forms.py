from django import forms
from .models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'email')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Comment'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('comment', 'author', 'text', 'email')
        widgets = {
            'comment': forms.HiddenInput(),
            'author': forms.TextInput(attrs={'placeholder': 'Name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Comment'}),
        }
