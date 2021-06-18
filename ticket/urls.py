from django.urls import path

from .views import TicketHomeView, TicketFormView

app_name = 'ticket'

urlpatterns = [
    path('',TicketHomeView.as_view(), name='ticket_home'),
    path('ticket_form/',TicketFormView.as_view(), name='ticket_form'),
]