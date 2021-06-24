from django.shortcuts import render
from django.views.generic import FormView

# from bug.forms import AssignDeveloperForm
# Create your views here.
def home(request):
    context = {
    }
    return render(request, 'project/project.html',context)


# class AssignView(FormView):
#     form_class    = AssignDeveloperForm
#     template_name = 'project/roles.html'
#     pass