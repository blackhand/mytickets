# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from common.models import AuditableModel, NamedModel

from sorl.thumbnail.fields import ImageWithThumbnailsField


 # Location Models

class Country(NamedModel, AuditableModel):
    """ Country Model """

    class Meta:
        verbose_name = _(u'Pais')
        verbose_name_plural = _(u'Paises')


class Province(NamedModel, AuditableModel):
    """ Province Model """
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name = _(u'Provincia')
        verbose_name_plural = _(u'Provincias')


class Auditorium(NamedModel, AuditableModel):
    """ Auditorium Model"""
    country = models.ForeignKey(Country)
    province = models.ForeignKey(Province)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    address = models.TextField()

    class Meta:
        verbose_name = _(u'Auditorio')
        verbose_name_plural = _(u'Auditorios')


 # Event Models

class Category(NamedModel, AuditableModel):
    """ Category Model """

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')


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

    class Meta:
        verbose_name = _(u'Artista')
        verbose_name_plural = _(u'Artistas')


class Event(NamedModel, AuditableModel):
    """ Event Model """
    category = models.ForeignKey(Category, null=True)
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

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')

    @models.permalink
    def get_absolute_url(self):
        """
        URL for Events
        """
        return ('event_detail', [str(self.id)])


class Zone(NamedModel, AuditableModel):
    """ Zone Model """
    event = models.ForeignKey(Event)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = _(u'Zona')
        verbose_name_plural = _(u'Zonas')


class Profile(NamedModel, AuditableModel):
    user = models.ForeignKey(User, unique=True)
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
    sell_by = models.ForeignKey(User, null=True, blank=True, related_name='sell_ticket_set')
    bought_by = models.OneToOneField(User, null=True, blank=True, related_name='buy_ticket_set')
 
    class Meta:
        verbose_name = _(u'Ticket')
        verbose_name_plural = _(u'Tickets')

