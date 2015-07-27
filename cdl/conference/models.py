# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.conference.models import Conference


class ConferenceCategory(models.Model):
    """
    a category of the conference such as "DevOps", "IoT",
    "Free culture", will be used as a label.
    """

    conference = models.ForeignKey(Conference, verbose_name=_("conference"))

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=680, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Conference category")
        verbose_name_plural = _(u"Thématiques")
