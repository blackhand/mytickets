# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from common.models import AuditableModel, NamedModel

from sorl.thumbnail.fields import ImageWithThumbnailsField
from datetime import timedelta

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
    image = ImageWithThumbnailsField(
        upload_to='auditorium_images',
        thumbnail={'size': (200, 200)},
        extra_thumbnails={
            'icon': {'size': (16, 16), 'options': ['crop', 'upscale']},
            'small': {'size': (100, 100)},
            'large': {'size': (400, 400)},
            },
        null=True, blank=True
        )
    address = models.TextField()

    class Meta:
        verbose_name = _(u'Auditorio')
        verbose_name_plural = _(u'Auditorios')


 # Event Models
class CategoryManager(models.Manager):
    def with_ads(self):
        return self.exclude(event=None)


class Category(NamedModel, AuditableModel):
    """ Category Model """

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')

    objects = CategoryManager()


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
    is_prominent = models.BooleanField(default=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = ImageWithThumbnailsField(
        upload_to='event_images',
        thumbnail={'size': (300, 300)},
        extra_thumbnails={
            'icon': {'size': (16, 16), 'options': ['crop', 'upscale']},
            'small': {'size': (100, 100)},
            'medium': {'size': (200, 200)},
            'large': {'size': (400, 400)},
            },
        null=True, blank=True
        )

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')
        ordering = ['-created_at']

    def save(self):
        """
        overloaded save method to create the asociated presentations
        for the model
        """
        day = self.start_date
        while day < self.end_date:
            # check if exist the date in asoc presentations
            # create if does not exist
            try:
                self.presentation_set.get(day=day)
            except Presentation.DoesNotExist:
                presentation = Presentation(day=day)
                self.presentation_set.add(presentation)
            day += timedelta(1)

        super(Event, self).save()
                
    @models.permalink
    def get_absolute_url(self):
        """
        URL for Events
        """
        return ('event_detail', [str(self.id)])


class Presentation(models.Model):
    """ Presentation Model """
    event = models.ForeignKey(Event)
    day = models.DateField()
    start_hour = models.TimeField(blank=True, null=True)
    end_hour = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Horario de Presentacion'
        verbose_name_plural = 'Horario de Presentaciones'

    def __unicode__(self):
        return u"%s - %s - %s" % (self.event.name, self.day, self.start_hour, )
        

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
    presentation = models.ForeignKey(Presentation)
    zone = models.ForeignKey(Zone,
            limit_choices_to = {'event__exact': event}
            )
    sell_by = models.ForeignKey(User, null=True, blank=True, related_name='sell_ticket_set')
    bought_by = models.OneToOneField(User, null=True, blank=True, related_name='buy_ticket_set')
 
    class Meta:
        verbose_name = _(u'Ticket')
        verbose_name_plural = _(u'Tickets')

