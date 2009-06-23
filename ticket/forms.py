# -*- coding: UTF-8 -*-

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ticket.models import Zone


class TicketForm(forms.Form):
    DATE_CHOICES = (('','-----'),)
    zone = forms.ModelChoiceField(Zone.objects.none(), widget=forms.RadioSelect())
    date = forms.ChoiceField(choices=DATE_CHOICES)
    quantity = forms.IntegerField()
    
    def __init__(self, event, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['zone'].queryset = event.zones.all()



