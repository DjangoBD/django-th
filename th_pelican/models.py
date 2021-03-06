# coding: utf-8
from django.db import models
from django_th.models.services import Services


class Pelican(Services):

    """
        pelican model
    """
    title = models.CharField(max_length=80)
    url = models.URLField()
    tags = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    path = models.CharField(max_length=255)
    trigger = models.ForeignKey('TriggerService')

    class Meta:
        app_label = 'django_th'
        db_table = 'django_th_pelican'

    def __str__(self):
        return self.name

    def show(self):
        return "My Pelican {}".format(self.name)
