from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)