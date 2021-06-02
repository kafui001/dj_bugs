from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    context = {
    }
    return render(request, 'bug/task.html',context)


class TaskView(CreateView):
    model = Task
    template_name = 'bug/task.html'
    form_class = TaskForm
    success_url = reverse_lazy('bug:task')
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        # context['unassigned'] =
        # context['in_progress'] =
        # context['needs_review'] =
        # context['completed'] =
        return context
