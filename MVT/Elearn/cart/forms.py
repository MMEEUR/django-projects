from django import forms

CHOISES = [(i, str(i)) for i in range(1, 21)]

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOISES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
