# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import get_object_or_404

from ticket.models import Event
from ticket.constants import MAX_EVENTS_PER_PAGE

from datetime import date, timedelta

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

    start_date = event.start_date
    end_date = event.end_date

    while start_date <= end_date:
        dates.append(start_date)
        start_date += timedelta(days=1)

    extra_context = {
            'dates': dates,
            }

    return object_detail(request,
            queryset = queryset,
            object_id = event_id,
            template_object_name = 'event',
            extra_context = extra_context)


def buy_ticket(request):
    return HttpResponse('buy_ticket')


def buy_sucess(request):
    return HttpResponse('buy_sucess')
