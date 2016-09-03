from accounts.models import *
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password', 'password2']:
            self.fields[field_name].help_text = None


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'date_applied', 'paid' )


class ApplyIdForm(forms.ModelForm):
    class Meta:
        model = IdApplication
        exclude = ('user', 'paid', 'date_applied', )
