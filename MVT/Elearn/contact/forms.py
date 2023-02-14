from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', "data-error": "Name is required."}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', "data-error": "Valid email is required."}))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', "data-error": "Subject is required."}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', "data-error": "Phone is required."}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', "data-error": "Please,leave us a message."}))
