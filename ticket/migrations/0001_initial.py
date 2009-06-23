# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from ticket.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Province'
        db.create_table('ticket_province', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
        ))
        db.send_create_signal('ticket', ['Province'])
        
        # Adding model 'Ticket'
        db.create_table('ticket_ticket', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('presentation', models.ForeignKey(orm.Presentation)),
            ('zone', models.ForeignKey(orm.Zone)),
            ('sell_by', models.ForeignKey(orm['auth.User'], related_name='sell_ticket_set', null=True, blank=True)),
            ('bought_by', models.ForeignKey(orm['auth.User'], related_name='buy_ticket_set', null=True, blank=True)),
        ))
        db.send_create_signal('ticket', ['Ticket'])
        
        # Adding model 'Auditorium'
        db.create_table('ticket_auditorium', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('province', models.ForeignKey(orm.Province)),
            ('is_active', models.BooleanField(default=True)),
            ('description', models.TextField()),
            ('image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, null=True, thumbnail={'size':(200,200)}, blank=True)),
            ('address', models.TextField()),
        ))
        db.send_create_signal('ticket', ['Auditorium'])
        
        # Adding model 'Country'
        db.create_table('ticket_country', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
        ))
        db.send_create_signal('ticket', ['Country'])
        
        # Adding model 'Zone'
        db.create_table('ticket_zone', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('presentation', models.ForeignKey(orm.Presentation)),
            ('price', models.FloatField()),
            ('quantity', models.PositiveIntegerField()),
        ))
        db.send_create_signal('ticket', ['Zone'])
        
        # Adding model 'Category'
        db.create_table('ticket_category', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
        ))
        db.send_create_signal('ticket', ['Category'])
        
        # Adding model 'Presentation'
        db.create_table('ticket_presentation', (
            ('id', models.AutoField(primary_key=True)),
            ('event', models.ForeignKey(orm.Event)),
            ('day', models.DateField()),
            ('start_hour', models.TimeField(null=True, blank=True)),
            ('end_hour', models.TimeField(null=True, blank=True)),
        ))
        db.send_create_signal('ticket', ['Presentation'])
        
        # Adding model 'Event'
        db.create_table('ticket_event', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('category', models.ForeignKey(orm.Category, null=True)),
            ('artist', models.ForeignKey(orm.Artist)),
            ('auditorium', models.ForeignKey(orm.Auditorium, null=True, blank=True)),
            ('is_active', models.BooleanField(default=True)),
            ('is_prominent', models.BooleanField(default=False)),
            ('description', models.TextField()),
            ('start_date', models.DateField()),
            ('end_date', models.DateField()),
            ('image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'medium':{'size':(200,200)},'large':{'size':(400,400)},}, null=True, thumbnail={'size':(300,300)}, blank=True)),
        ))
        db.send_create_signal('ticket', ['Event'])
        
        # Adding model 'Artist'
        db.create_table('ticket_artist', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('biography', models.TextField()),
            ('image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, null=True, thumbnail={'size':(200,200)}, blank=True)),
        ))
        db.send_create_signal('ticket', ['Artist'])
        
        # Adding model 'Profile'
        db.create_table('ticket_profile', (
            ('id', models.AutoField(primary_key=True)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('user', models.ForeignKey(orm['auth.User'], unique=True)),
            ('province', models.ForeignKey(orm.Province)),
            ('country', models.ForeignKey(orm.Country)),
            ('address', models.TextField()),
        ))
        db.send_create_signal('ticket', ['Profile'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Province'
        db.delete_table('ticket_province')
        
        # Deleting model 'Ticket'
        db.delete_table('ticket_ticket')
        
        # Deleting model 'Auditorium'
        db.delete_table('ticket_auditorium')
        
        # Deleting model 'Country'
        db.delete_table('ticket_country')
        
        # Deleting model 'Zone'
        db.delete_table('ticket_zone')
        
        # Deleting model 'Category'
        db.delete_table('ticket_category')
        
        # Deleting model 'Presentation'
        db.delete_table('ticket_presentation')
        
        # Deleting model 'Event'
        db.delete_table('ticket_event')
        
        # Deleting model 'Artist'
        db.delete_table('ticket_artist')
        
        # Deleting model 'Profile'
        db.delete_table('ticket_profile')
        
    
    
    models = {
        'ticket.province': {
            'country': ('models.ForeignKey', ["orm['ticket.Country']"], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.ticket': {
            'bought_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': "'buy_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'presentation': ('models.ForeignKey', ["orm['ticket.Presentation']"], {}),
            'sell_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': "'sell_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'zone': ('models.ForeignKey', ["orm['ticket.Zone']"], {'limit_choices_to': "{'presentation__exact':presentation}"})
        },
        'ticket.auditorium': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ["orm['ticket.Country']"], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('ImageWithThumbnailsField', [], {'extra_thumbnails': "{'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}", 'null': 'True', 'thumbnail': "{'size':(200,200)}", 'blank': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ["orm['ticket.Province']"], {}),
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
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'presentation': ('models.ForeignKey', ["orm['ticket.Presentation']"], {}),
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
        'ticket.profile': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ["orm['ticket.Country']"], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ["orm['ticket.Province']"], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {'unique': 'True'})
        },
        'ticket.presentation': {
            'Meta': {'ordering': "['day']"},
            'day': ('models.DateField', [], {}),
            'end_hour': ('models.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('models.ForeignKey', ["orm['ticket.Event']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'start_hour': ('models.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'ticket.event': {
            'Meta': {'ordering': "['-created_at']"},
            'artist': ('models.ForeignKey', ["orm['ticket.Artist']"], {}),
            'auditorium': ('models.ForeignKey', ["orm['ticket.Auditorium']"], {'null': 'True', 'blank': 'True'}),
            'category': ('models.ForeignKey', ["orm['ticket.Category']"], {'null': 'True'}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('ImageWithThumbnailsField', [], {'extra_thumbnails': "{'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'medium':{'size':(200,200)},'large':{'size':(400,400)},}", 'null': 'True', 'thumbnail': "{'size':(300,300)}", 'blank': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'is_prominent': ('models.BooleanField', [], {'default': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'start_date': ('models.DateField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.artist': {
            'biography': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('ImageWithThumbnailsField', [], {'extra_thumbnails': "{'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}", 'null': 'True', 'thumbnail': "{'size':(200,200)}", 'blank': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        }
    }
    
    complete_apps = ['ticket']
