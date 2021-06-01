from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from bug.models import BugUser

class UserSignUpForm(UserCreationForm):
    email       = forms.EmailField()
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)
    
    class Meta:
        model = BugUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']