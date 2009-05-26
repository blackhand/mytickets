# -*- coding: UTF-8 -*-

from django.db import models

from datetime import datetime



class AuditableManager(models.Manager):
    """
    Replacement for the default manager in AuditableModels 
    so we only query for the active objects.
    """
    def get_query_set(self):
        """
        Override the all() method to query only active models
        """
        return super(AuditableManager, self).get_query_set().filter(is_deleted=False)

    def all_deleted(self):
        """
        Helper method to obtain deleted items
        """
        return super(AuditableManager, self).get_query_set().filter(is_deleted=True)


class AuditableModel(models.Model):
    created_at = models.DateTimeField(
            u"Fecha de Creacion",
            auto_now_add=True, 
            editable=False)

    updated_at = models.DateTimeField(
            u"Fecha de Modificacion",
            auto_now=True,
            editable=False)

    is_deleted = models.BooleanField(
            default=False,
            editable=False)

    objects = AuditableManager()

    def delete(self):
        """ 
        Overrides the default deleve() method so we don't delete models
        from the database,
        """
        self.is_deleted = True
        self.deleted = datetime.now()
        self.save()
 
    class Meta:
        abstract = True


class NamedModel(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s" % (self.name, )

    class Meta:
        abstract = True
