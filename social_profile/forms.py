from django.forms import ModelForm
from .models import SocialProfile
from django.contrib.auth.models import User
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class RegistrationForm(ModelForm):

    class Meta:

        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(ModelForm):

    class Meta:

        model = SocialProfile
        exclude = ['user', 'status', 'date_added']
        widgets = {
            'date_of_birth': myDateInput
        }








