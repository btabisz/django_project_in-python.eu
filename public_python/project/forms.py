from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import forms as auth_forms


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'size': 24}), max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = auth_forms.ReadOnlyPasswordHashField(label="Password")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

