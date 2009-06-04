# -*- coding: UTF-8 -*-

from south.db import db
from django.db import models
from ticket.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('ticket_profile', (
            ('province', models.ForeignKey(orm.Province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.Country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('user', models.ForeignKey(orm['auth.User'], unique=True)),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['Profile'])
        
        # Deleting model 'seller'
        db.delete_table('ticket_seller')
        
        # Deleting model 'buyer'
        db.delete_table('ticket_buyer')
        
        # Changing field 'Ticket.sell_by'
        db.alter_column('ticket_ticket', 'sell_by_id', models.ForeignKey(orm['auth.User'], null=True, blank=True))
        
        # Changing field 'Ticket.bought_by'
        db.alter_column('ticket_ticket', 'bought_by_id', models.OneToOneField(orm['auth.User'], null=True, blank=True))
        
        # Changing field 'Event.image'
        db.alter_column('ticket_event', 'image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, null=True, thumbnail={'size':(200,200)}, blank=True))
        
        # Changing field 'Artist.image'
        db.alter_column('ticket_artist', 'image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, null=True, thumbnail={'size':(200,200)}, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('ticket_profile')
        
        # Adding model 'seller'
        db.create_table('ticket_seller', (
            ('province', models.ForeignKey(orm.province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('user', models.OneToOneField(orm['auth.user'])),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['seller'])
        
        # Adding model 'buyer'
        db.create_table('ticket_buyer', (
            ('province', models.ForeignKey(orm.province)),
            ('is_deleted', models.BooleanField(default=False, editable=False)),
            ('name', models.CharField(max_length=64)),
            ('country', models.ForeignKey(orm.country)),
            ('created_at', models.DateTimeField(u"Fecha de Creacion", auto_now_add=True, editable=False)),
            ('updated_at', models.DateTimeField(u"Fecha de Modificacion", auto_now=True, editable=False)),
            ('user', models.OneToOneField(orm['auth.user'])),
            ('address', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('ticket', ['buyer'])
        
        # Changing field 'Ticket.sell_by'
        db.alter_column('ticket_ticket', 'sell_by_id', models.ForeignKey(Seller, null=True, blank=True))
        
        # Changing field 'Ticket.bought_by'
        db.alter_column('ticket_ticket', 'bought_by_id', models.OneToOneField(Buyer, null=True, blank=True))
        
        # Changing field 'Event.image'
        db.alter_column('ticket_event', 'image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, thumbnail={'size':(200,200)}))
        
        # Changing field 'Artist.image'
        db.alter_column('ticket_artist', 'image', ImageWithThumbnailsField(extra_thumbnails={'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}, thumbnail={'size':(200,200)}))
        
    
    
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
            'bought_by': ('models.OneToOneField', ['User'], {'related_name': "'buy_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'event': ('models.ForeignKey', ['Event'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'sell_by': ('models.ForeignKey', ['User'], {'related_name': "'sell_ticket_set'", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'zone': ('models.ForeignKey', ['Zone'], {'limit_choices_to': "{'event__exact':event}"})
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
        'ticket.profile': {
            'address': ('models.TextField', [], {}),
            'country': ('models.ForeignKey', ['Country'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'province': ('models.ForeignKey', ['Province'], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'}),
            'user': ('models.ForeignKey', ['User'], {'unique': 'True'})
        },
        'ticket.event': {
            'artist': ('models.ForeignKey', ['Artist'], {}),
            'auditorium': ('models.ForeignKey', ['Auditorium'], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'description': ('models.TextField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('ImageWithThumbnailsField', [], {'extra_thumbnails': "{'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}", 'null': 'True', 'upload_to': "'event_images'", 'thumbnail': "{'size':(200,200)}", 'blank': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'start_date': ('models.DateField', [], {}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        },
        'ticket.artist': {
            'biography': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', ['u"Fecha de Creacion"'], {'auto_now_add': 'True', 'editable': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('ImageWithThumbnailsField', [], {'extra_thumbnails': "{'icon':{'size':(16,16),'options':['crop','upscale']},'small':{'size':(100,100)},'large':{'size':(400,400)},}", 'null': 'True', 'upload_to': "'artist_images'", 'thumbnail': "{'size':(200,200)}", 'blank': 'True'}),
            'is_deleted': ('models.BooleanField', [], {'default': 'False', 'editable': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'updated_at': ('models.DateTimeField', ['u"Fecha de Modificacion"'], {'auto_now': 'True', 'editable': 'False'})
        }
    }
    
    complete_apps = ['ticket']
