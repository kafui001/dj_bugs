from django.shortcuts import render
from django.views.generic import ListView, FormView

from .forms import TicketForm
from bug.models import Ticket
# Create your views here.

class TicketHomeView(FormView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket/ticket.html'
    queryset = Ticket.objects.all

    def get_context_data(self, **kwargs):
        context = super(TicketHomeView, self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all()
        return context