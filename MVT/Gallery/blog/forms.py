from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model       = Comment
        fields      = ('body',)
        exclude     = ('active', 'post', 'created', 'updated')

        
#class CommentForm(forms.ModelForm):
#    class Meta:
#       model       = Comment
#       fields      = ('name', 'email', 'body')
#       exclude     = ('active', 'post', 'created', 'updated')
#       widgets = {
#           'name':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
#           'email':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
#          'body':     forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر'}),
#       }  
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','id': 'search'}))