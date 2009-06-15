# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from common.shortcuts import render_response
from ticket.models import Event, Presentation, Ticket, Zone
from ticket.forms import TicketForm
from ticket.constants import MAX_EVENTS_PER_PAGE


def homepage(request):
    return event_list(request)

def event_list(request,
               category=None,
               country=None,
               province=None,
               auditorium=None
        ):
    """
    this view provide a full event list, filtered based
    """

    queryset = Event.objects.all()
    if category is not None:
        queryset = queryset.filter(category__name=category)
    extra_context = {}

    return object_list(request,
            queryset=queryset,
            paginate_by=MAX_EVENTS_PER_PAGE,
            extra_context=extra_context)


def event_detail(request, event_id):
    """
    this view manage the detail for and event
    """
    queryset = Event.objects.all()
    dates = list()
    event = get_object_or_404(Event, id=event_id)

    extra_context = {}
    
    return object_detail(request,
            queryset = queryset,
            object_id = event_id,
            template_object_name = 'event',
            extra_context = extra_context)


@login_required
def buy_ticket(request, presentation_id):
    """
    View that process the buy process
    """
    presentation = get_object_or_404(Presentation, id=presentation_id)

    zones = presentation.zone_set.filter(quantity__gt=0)

    if request.method == 'POST':
        form = TicketForm(presentation, request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            for t in range(0,quantity):
                ticket = Ticket(
                    presentation = presentation,
                    zone = form.cleaned_data['zone'],
                    bought_by = request.user,
                    )
                ticket.save()
                zone = ticket.zone
                zone.quantity -= 1
                zone.save()
            
            return HttpResponseRedirect(
                    reverse(
                        'buy_sucess',
                        args=[str(presentation.id), str(zone.id)]))
            

    form = TicketForm(presentation)
    extra_context = {
            'event': presentation.event,
            'form': form
            }

    return render_response(
            request,
            'ticket/buy_ticket.html',
            extra_context
            )


def buy_sucess(request, presentation_id, zone_id):
    presentation = get_object_or_404(Presentation, id=presentation_id)
    zone = get_object_or_404(Zone, id=zone_id)

    extra_context = {
            'event': presentation.event,
            'presentation': presentation,
            'zone': zone,
            }

    return render_response(
            request,
            'ticket/buy_sucess.html',
            extra_context
            )
