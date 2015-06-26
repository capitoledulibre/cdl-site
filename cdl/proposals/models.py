from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import ProposalBase



class ProposalCategory(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Capitole du Libre proposal category")
        verbose_name_plural = _(u"Capitole du Libre proposal categories")


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, _(u"Novice")),
        (AUDIENCE_LEVEL_INTERMEDIATE, _(u"Intermediate")),
        (AUDIENCE_LEVEL_EXPERIENCED, _(u"Experienced")),
    ]
    
    category = models.ForeignKey(ProposalCategory)

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text=_(u"By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.")
    )
    
    def __unicode__(self):
        return u"#%s - %s (%s)" % (self.number, self.title, self.speaker)

    class Meta:
        abstract = True


class TalkProposal(Proposal):

    DURATION_CHOICES = [
        (0, _(u"No preference")),
        (1, _(u"I prefer a 20 minute slot")),
        (2, _(u"I prefer a 50 minute slot")),
    ]

    duration = models.IntegerField(choices=DURATION_CHOICES)

    class Meta:
        verbose_name = _(u"talk proposal")


class TutorialProposal(Proposal):

    DURATION_CHOICES = [
        (0, _(u"No preference")),
        (1, _(u"I prefer a 1h30 slot")),
        (2, _(u"I prefer a 3h slot")),
    ]

    duration = models.IntegerField(choices=DURATION_CHOICES)

    class Meta:
        verbose_name = _(u"tutorial proposal")


class StandProposal(ProposalBase):

    organisation = models.CharField(max_length=150)

    def __unicode__(self):
        return u"#%s - %s (%s)" % (self.number, self.title, self.speaker)

    class Meta:
        verbose_name = _(u"stand proposal")
