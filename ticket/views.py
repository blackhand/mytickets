from django.shortcuts import render_to_response
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('homepage')

def event_list(request,
               country=None,
               province=None,
               auditorium=None
        ):
    return HttpResponse('event_list')

def event_detail(request):
    return HttpResponse('event_detail')

def buy_ticket(request):
    return HttpResponse('buy_ticket')

def buy_sucess(request):
    return HttpResponse('buy_sucess')
