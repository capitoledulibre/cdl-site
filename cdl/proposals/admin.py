from django.contrib import admin

from .models import TalkProposal, TutorialProposal, StandProposal

admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(StandProposal)
