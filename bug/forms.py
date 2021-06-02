from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import ProjectManager, Developer, Task
from .models import Task,  ProjectManager, Developer, TaskPriority, TaskStatus




# priority_choices = TaskPriority.objects.all().values_list('name','name')
# priority_choice_list = []
# for item in priority_choices:
#     priority_choice_list.append(item)


# status_choices = TaskStatus.objects.all().values_list('name','name')
# status_choice_list = []
# for item in status_choices:
#     status_choice_list.append(item)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
           'description'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',                            
                'placeholder':'title of your post',
                'id':"exampleFormControlInput77"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'add any extra details here',
                'id':"exampleFormControlTextarea78",
                'rows':"5"
                }
            ),
        }