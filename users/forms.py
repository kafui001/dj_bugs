from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from bug.models import BugUser

class UserSignUpForm(UserCreationForm):
    email       = forms.EmailField()
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)
    
    class Meta:
        model = BugUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        fields = [
            'username',
           'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'type':"email",
                'class': 'form-control form-control-lg' ,                            
                'placeholder':'username',
                }
            ),
            
            'password': forms.TextInput(attrs={
                'type':"password",
                'class': 'form-control form-control-lg' ,                            
                'placeholder':'***************',
                # 'id':"exampleFormControlInput77"
                }
            )
        }