from django import forms
from .models import AppUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):

	email = forms.EmailField()
	class Meta():
		model = User
		fields = ('username', 'firstname', 'lastname', 'password1', 'password2', 'email')

		