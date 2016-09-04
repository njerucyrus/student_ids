from django import forms


class PaymentForm(forms.Form):
    phoneNumber = forms.CharField(label="Phone Number", max_length=13, required=True)
