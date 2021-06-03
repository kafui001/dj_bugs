from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    context = {
    }
    return render(request, 'bug/task.html',context)


class TaskView(FormView):
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

    # limit task creation to only admin and project manager
    def form_valid(self, form):
        form = form.save(commit=False)
        if self.request.user.is_project_manager or self.request.user.is_superuser:
            form.creator = self.request.user
            form.save()
            print(form.creator)
            print(form.priority)
            return super(TaskView, self).form_valid(form)
        else:
            print("you are not authorized to create a task")
            # fix this section