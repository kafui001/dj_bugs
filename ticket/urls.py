from django.urls import path

from .views import TicketHomeView

app_name = 'ticket'

urlpatterns = [
    path('',TicketHomeView.as_view(), name='ticket_home'),
]