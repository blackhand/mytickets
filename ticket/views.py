# -*- coding: UTF-8 -*-

from common.shortcuts import render_response

from django.http import HttpResponse
from django.views.generic.list_detail import object_list, object_detail

from ticket.models import Event

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
            queryset = queryset,
            extra_context = extra_context)


def event_detail(request, event_id):
    """
    this view manage the detail for and event
    """
    queryset = Event.objects.all()
    extra_context = {}
    return object_detail(request,
            queryset = queryset,
            object_id = event_id,
            template_object_name = 'event',
            extra_context = extra_context)


def buy_ticket(request):
    return HttpResponse('buy_ticket')


def buy_sucess(request):
    return HttpResponse('buy_sucess')
