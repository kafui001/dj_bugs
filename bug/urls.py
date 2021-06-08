from django.urls import path

from .views import home, TaskView, TaskDetailView

app_name = 'bug'

urlpatterns = [
    # path('', home, name='home'),
    path('', TaskView.as_view(), name='task'),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]