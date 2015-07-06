from django.contrib import admin

from .models import ProposalCategory, TalkProposal, TutorialProposal, StandProposal

class ProposalCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ProposalCategory, ProposalCategoryAdmin)
admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(StandProposal)
