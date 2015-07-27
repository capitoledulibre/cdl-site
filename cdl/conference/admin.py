from django.contrib import admin

from .models import ConferenceCategory

class ConferenceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ConferenceCategory, ConferenceCategoryAdmin)
