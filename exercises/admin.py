from django.contrib import admin
from .models import BonusLink, BonusView

from .models import SubmittableExercise, GeneratedExercise, Submission, FileSubmission

admin.site.register(Submission)
admin.site.register(FileSubmission)
admin.site.register(SubmittableExercise)
admin.site.register(GeneratedExercise)

@admin.register(BonusLink)
class BonusLinkAdmin(admin.ModelAdmin):
    list_display = ('secret',)

@admin.register(BonusView)
class BonusViewAdmin(admin.ModelAdmin):
    list_display = ('link', 'user', 'date_viewed')

