from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import ProjectManager, Developer, Task
from .models import Task




# priority_choices = Priority.objects.all().values_list('name','name')
# priority_choice_list = []
# for item in priority_choices:
#     priority_choice_list.append(item)


# status_choices = Status.objects.all().values_list('name','name')
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