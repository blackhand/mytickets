# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User

from common.models import AuditableModel, NamedModel

from sorl.thumbnail.fields import ImageWithThumbnailsField


 # Location Models

class Country(NamedModel, AuditableModel):
    """ Country Model """


class Province(NamedModel, AuditableModel):
    """ Province Model """
    country = models.ForeignKey(Country)


class Auditorium(NamedModel, AuditableModel):
    """ Auditorium Model"""
    country = models.ForeignKey(Country)
    province = models.ForeignKey(Province)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    address = models.TextField()


 # Event Models

class Category(NamedModel, AuditableModel):
    """ Category Model """


class Artist(NamedModel, AuditableModel):
    """ Artist Model """
    biography = models.TextField()
    image = ImageWithThumbnailsField(
        upload_to='artist_images',
        thumbnail={'size': (200, 200)},
        extra_thumbnails={
            'icon': {'size': (16, 16), 'options': ['crop', 'upscale']},
            'small': {'size': (100, 100)},
            'large': {'size': (400, 400)},
            },
        null=True, blank=True
        )


class Event(NamedModel, AuditableModel):
    """ Event Model """
    artist = models.ForeignKey(Artist)
    auditorium = models.ForeignKey(Auditorium)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = ImageWithThumbnailsField(
        upload_to='event_images',
        thumbnail={'size': (200, 200)},
        extra_thumbnails={
            'icon': {'size': (16, 16), 'options': ['crop', 'upscale']},
            'small': {'size': (100, 100)},
            'large': {'size': (400, 400)},
            },
        null=True, blank=True
        )


class Zone(NamedModel, AuditableModel):
    """ Zone Model """
    event = models.ForeignKey(Event)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()


class Seller(NamedModel, AuditableModel):
    """ Seller (POS) Model """
    user = models.OneToOneField(User)
    province = models.ForeignKey(Province)
    country = models.ForeignKey(Country)
    address = models.TextField()


class Buyer(NamedModel, AuditableModel):
    user = models.OneToOneField(User)
    province = models.ForeignKey(Province)
    country = models.ForeignKey(Country)
    address = models.TextField()


class Ticket(NamedModel, AuditableModel):
    """ Ticket Model """
    GENERATED = 0
    RESERVED = 1
    BUYED = 2
    CANCELLED = 3
    STATUS_CHOICES = {
            GENERATED: 'Generado',
            RESERVED: 'En Reserva',
            BUYED: 'Comprado',
            CANCELLED: 'Cancelado',
    }

    event = models.ForeignKey(Event)
    zone = models.ForeignKey(Zone,
            limit_choices_to = {'event__exact': event}
            )
    sell_by = models.ForeignKey(Seller, null=True, blank=True)
    bought_by = models.OneToOneField(Buyer, null=True, blank=True)
  




