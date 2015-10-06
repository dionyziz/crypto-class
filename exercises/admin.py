from django.contrib import admin
from .models import BonusLink, BonusView

@admin.register(BonusLink)
class BonusLinkAdmin(admin.ModelAdmin):
    list_display = ('secret',)

@admin.register(BonusView)
class BonusViewAdmin(admin.ModelAdmin):
    list_display = ('link', 'user', 'date_viewed')
