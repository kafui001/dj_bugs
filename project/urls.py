from django.urls import path

from .views import  home

app_name = 'project'

urlpatterns = [
    path('', home, name='project_home'),
    # path('edit/<int:pk>/',TaskEditView.as_view(), name='task_edit'),
    # path('delete/<int:pk>/',TaskDeleteView.as_view(), name='task_delete'),
    # path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]