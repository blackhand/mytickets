# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from ticket.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Presentation'
        db.create_table('ticket_presentation', (
            ('id', models.AutoField(primary_key=True)),
            ('event', models.ForeignKey(orm.Event)),
            ('day', models.DateField()),
            ('start_hour', models.TimeField(null=True, blank=True)),
            ('end_hour', models.TimeField(null=True, blank=True)),
        ))
        db.send_create_signal('ticket', ['Presentation'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Presentation'
        db.delete_table('ticket_presentation')
        
    
    
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
            'bought_by': ('models.OneToOneField', ["orm['auth.User']"], {'related_name': "'buy_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'event': ('models.ForeignKey', ["orm['ticket.Event']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'sell_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': "'sell_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'zone': ('models.ForeignKey', ["orm['ticket.Zone']"], {'limit_choices_to': "{'event__exact':event}"})
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
            'event': ('models.ForeignKey', ["orm['ticket.Event']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'price': ('models.FloatField', [], {}),
            'quantity': ('models.PositiveIntegerField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.presentation': {
            'day': ('models.DateField', [], {}),
            'end_hour': ('models.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('models.ForeignKey', ["orm['ticket.Event']"], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'start_hour': ('models.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'ticket.category': {
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.event': {
            'Meta': {'ordering': "['-created_at']"},
            'artist': ('models.ForeignKey', ["orm['ticket.Artist']"], {}),
            'auditorium': ('models.ForeignKey', ["orm['ticket.Auditorium']"], {}),
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
        }
    }
    
    complete_apps = ['ticket']
