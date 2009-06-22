# -*- coding: UTF-8 -*-

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ticket.models import Zone


class TicketForm(forms.Form):
    zone = forms.ModelChoiceField(Zone.objects.none(), widget=forms.RadioSelect())
    date = forms.ChoiceField(choices=((,)(,))
    quantity = forms.IntegerField()
    
    def __init__(self, event, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        for 
        
        self.fields['zone'].queryset = event.zones.all()



