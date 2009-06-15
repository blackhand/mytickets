# -*- coding: UTF-8 -*-

from django import forms
from ticket.models import Zone


class TicketForm(forms.Form):
    zone = forms.ModelChoiceField(Zone.objects.none(), widget=forms.RadioSelect())
    quantity = forms.IntegerField()
    
    def __init__(self, position, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['zone'].queryset = position.zone_set.filter(quantity__gt=0)

