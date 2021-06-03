from django.urls import path

from .views import home, TaskView

app_name = 'bug'

urlpatterns = [
    # path('', home, name='home'),
    path('', TaskView.as_view(), name='task'),
]