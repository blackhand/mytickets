# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from ticket.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Province'
        db.create_table('ticket_province', (
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['Province'])
        
        # Adding model 'Ticket'
        db.create_table('ticket_ticket', (
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('zone', models.ForeignKey(orm.Zone)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('sell_by', models.ForeignKey(orm.Seller, null=True, blank=True)),
            ('event', models.ForeignKey(orm.Event)),
        ))
        db.send_create_signal('ticket', ['Ticket'])
        
        # Adding model 'Seller'
        db.create_table('ticket_seller', (
            ('province', models.ForeignKey(orm.Province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('user', models.OneToOneField(orm['auth.User'])),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['Seller'])
        
        # Adding model 'Auditorium'
        db.create_table('ticket_auditorium', (
            ('province', models.ForeignKey(orm.Province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('is_active', models.BooleanField(default=True)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
            ('description', models.TextField()),
        ))
        db.send_create_signal('ticket', ['Auditorium'])
        
        # Adding model 'Country'
        db.create_table('ticket_country', (
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=64)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
        ))
        db.send_create_signal('ticket', ['Country'])
        
        # Adding model 'Zone'
        db.create_table('ticket_zone', (
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('price', models.FloatField()),
            ('event', models.ForeignKey(orm.Event)),
            ('quantity', models.PositiveIntegerField()),
        ))
        db.send_create_signal('ticket', ['Zone'])
        
        # Adding model 'Category'
        db.create_table('ticket_category', (
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=64)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
        ))
        db.send_create_signal('ticket', ['Category'])
        
        # Adding model 'Buyer'
        db.create_table('ticket_buyer', (
            ('province', models.ForeignKey(orm.Province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('user', models.OneToOneField(orm['auth.User'])),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['Buyer'])
        
        # Adding model 'Event'
        db.create_table('ticket_event', (
            ('province', models.ForeignKey(orm.Province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('end_date', models.DateField()),
            ('artist', models.ForeignKey(orm.Artist)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('description', models.TextField()),
            ('is_active', models.BooleanField(default=True)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('start_date', models.DateField()),
            ('id', models.AutoField(primary_key=True)),
            ('auditorium', models.ForeignKey(orm.Auditorium)),
        ))
        db.send_create_signal('ticket', ['Event'])
        
        # Adding model 'Artist'
        db.create_table('ticket_artist', (
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('biography', models.TextField()),
        ))
        db.send_create_signal('ticket', ['Artist'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Province'
        db.delete_table('ticket_province')
        
        # Deleting model 'Ticket'
        db.delete_table('ticket_ticket')
        
        # Deleting model 'Seller'
        db.delete_table('ticket_seller')
        
        # Deleting model 'Auditorium'
        db.delete_table('ticket_auditorium')
        
        # Deleting model 'Country'
        db.delete_table('ticket_country')
        
        # Deleting model 'Zone'
        db.delete_table('ticket_zone')
        
        # Deleting model 'Category'
        db.delete_table('ticket_category')
        
        # Deleting model 'Buyer'
        db.delete_table('ticket_buyer')
        
        # Deleting model 'Event'
        db.delete_table('ticket_event')
        
        # Deleting model 'Artist'
        db.delete_table('ticket_artist')
        
    
    
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
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'event': ('models.ForeignKey', ['Event'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'sell_by': ('models.ForeignKey', ['Seller'], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'zone': ('models.ForeignKey', ['Zone'], {'limit_choices_to': "{'event__exact':event}"})
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
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ['Province'], {}),
            'start_date': ('models.DateField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.artist': {
            'biography': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        }
    }
    
    complete_apps = ['ticket']
