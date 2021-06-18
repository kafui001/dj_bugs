from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import TicketForm
from bug.models import Ticket
# Create your views here.

class TicketHomeView(ListView):
    model = Ticket
    # form_class = TicketForm
    template_name = 'ticket/ticket.html'
    # queryset = Ticket.objects.all

    def get_context_data(self, **kwargs):
        context = super(TicketHomeView, self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all()
        return context

# accepting form from custom template tag(ticket_form.html)
class TicketFormView(FormView):
    model = Ticket
    # template_name = 'bug/task.html'
    form_class = TicketForm
    success_url = reverse_lazy('ticket:ticket_home')

    def form_valid(self, form):
        print("##################")
        
        form = form.save(commit=False)
        form.creator = self.request.user
        form.status = 'open'
        form.save()
        print(form.creator)
        print(form.priority)

        return super(TicketFormView, self).form_valid(form)
        