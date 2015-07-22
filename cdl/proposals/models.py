from django.db import models
from django.utils.translation import ugettext_lazy as _

from multiselectfield.db.fields import MultiSelectField

from symposion.proposals.models import ProposalBase


class ProposalCategory(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=680, blank=True)

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

    VIDEO_OUTPUT = (
        ("VGA", u"VGA"),
        ("DVI", u"DVI"),
        ("HDMI", u"HDMI"),
        ("DPORT", u"Display Port"),
        ("MDPORT", u" Mini Display Port"),
    )

    category = models.ForeignKey(ProposalCategory)

    audience_level = models.IntegerField(
        _("Audience level"),
        choices=AUDIENCE_LEVELS)

    prerequistes = models.TextField(
        _("Prerequistes"),
        help_text=_("If Prerequistes are needed to follow this talk or workshop."),
        blank=True
    )

    video_output = MultiSelectField(
        _("Video output"),
        choices=VIDEO_OUTPUT,
        help_text=_("Specify video output."),
        blank=True,
    )

    broadcast_audio = models.BooleanField(
        _("Broadcast audio"),
        default=None,
        help_text=_(u"Do you need audio material to broadcast audio ?")
    )

    recording_release = models.BooleanField(
        _("Recording release"),
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

    duration = models.IntegerField(_("Duration"), choices=DURATION_CHOICES)

    class Meta:
        verbose_name = _(u"talk proposal")


class TutorialProposal(Proposal):

    DURATION_CHOICES = [
        (0, _(u"No preference")),
        (1, _(u"I prefer a 1h20 slot")),
        (2, _(u"I prefer a 2h50 slot")),
    ]

    duration = models.IntegerField(_("Duration"), choices=DURATION_CHOICES)

    class Meta:
        verbose_name = _(u"tutorial proposal")


class StandProposal(ProposalBase):

    organisation = models.CharField(max_length=150)

    def __unicode__(self):
        return u"#%s - %s (%s)" % (self.number, self.title, self.speaker)

    class Meta:
        verbose_name = _(u"stand proposal")
