# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from ticket.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Ticket.bought_by'
        db.add_column('ticket_ticket', 'bought_by', models.OneToOneField(orm.Buyer, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Ticket.bought_by'
        db.delete_column('ticket_ticket', 'bought_by_id')
        
    
    
    models = {
        'ticket.province': {
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.ticket': {
            'bought_by': ('models.OneToOneField', ['Buyer'], {'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'event': ('models.ForeignKey', ['Event'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'sell_by': ('models.ForeignKey', ['Seller'], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'zone': ('models.ForeignKey', ['Zone'], {'limit_choices_to': "{'event__exact':event}"})
        },
        'ticket.artist': {
            'biography': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.auditorium': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ['Province'], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'ticket.country': {
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.zone': {
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'event': ('models.ForeignKey', ['Event'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'price': ('models.FloatField', [], {}),
            'quantity': ('models.PositiveIntegerField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.category': {
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.buyer': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ['Province'], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'user': ('models.OneToOneField', ['User'], {})
        },
        'ticket.event': {
            'artist': ('models.ForeignKey', ['Artist'], {}),
            'auditorium': ('models.ForeignKey', ['Auditorium'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'start_date': ('models.DateField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.seller': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ['Province'], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'user': ('models.OneToOneField', ['User'], {})
        }
    }
    
    complete_apps = ['ticket']
