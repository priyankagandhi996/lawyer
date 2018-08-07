from django import forms
from.models import Lawyer ,Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Lawyer_register(forms.ModelForm):
    class Meta:
        model=Lawyer
        fields=['city','issues','phone_number']


class CreateUser(UserCreationForm):

    class Meta:
        model=User
        fields=['username','password1','password2','email']
