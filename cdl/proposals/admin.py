from django.contrib import admin

from .models import ProposalCategory, TalkProposal, TutorialProposal, StandProposal


admin.site.register(ProposalCategory)
admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(StandProposal)
