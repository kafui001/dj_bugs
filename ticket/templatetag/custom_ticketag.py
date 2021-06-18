from django import template
from ticket.forms import TicketForm
# template_tag is registered in dj_bugs/settings.py under TEMPLATES
register = template.Library()


@register.inclusion_tag('ticket/ticket_form.html', takes_context=True)
def show_ticket_form(context):
    request_user = context['request'].user
    ticket_form = TicketForm()
    return {'form':ticket_form}