# -*- coding: UTF-8 -*-

from django import forms
from ticket.models import Zone

from dateutil import parser

class TicketForm(forms.Form):
    QTY_CHOICES = [(r, unicode(r)) for r in range(1,11)]
    date = forms.ChoiceField()
    zone = forms.ModelChoiceField(Zone.objects.none())
    quantity = forms.ChoiceField(choices=QTY_CHOICES)
    
    def __init__(self, event, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        dates = event.date_list
        self.fields['date'].choices = [(dates.index(x),x.strftime('%d-%m-%Y')) for x in dates]
        self.fields['zone'].queryset = event.zone_list.all()

    def clean_date(self):
        data = self.cleaned_data['date']
        return parser.parse(self.fields['date'].choices[int(data)][1]).date()

    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        return int(data)

