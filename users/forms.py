from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from bug.models import BugUser, Developer, ProjectManager, Administrator

assign_admin = Administrator.objects.all().values_list('admin','admin')
admin_list = []
for user in assign_admin:
    admin_list.append(user)



assign_pm = ProjectManager.objects.all().values_list('admin','admin')
pm_list = []
for user in assign_pm:
    pm_list.append(user)




assign_dev = Developer.objects.all().values_list('admin','admin')
dev_list = []
for user in assign_dev:
    dev_list.append(user)

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


class AdminForm(forms.ModelForm):
    class Meta:
        model  = Administrator
        fields = ['user']

        widgets = {
            'user': forms.Select(choices=admin_list, attrs={
                'class': 'form-control',
                
                }
            ),
        }


class DevForm(forms.ModelForm):
    class Meta:
        model  = Developer
        fields = ['user','project_manager']

        widgets = {
            'user': forms.Select(choices=dev_list, attrs={
                'class': 'form-control',
                }
            ),
            'pm': forms.Select(choices=pm_list, attrs={
                'class': 'form-control',
                }
            ),
        }

class PmForm(forms.ModelForm):
    class Meta:
        model  = ProjectManager
        fields = ['user']

        widgets = {
            'user': forms.Select(choices=pm_list, attrs={
                'class': 'form-control',
                }
            ),
        }