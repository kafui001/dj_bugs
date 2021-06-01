from django.urls import path

from .views import home

app_name = 'bug'

urlpatterns = [
    path('', home, name='home'),
]