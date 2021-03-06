# -*- coding: utf8 -*-
import os.path

from django.conf import settings
from django.contrib import admin, messages
from django.http import HttpResponse

from .models import BonusLink, BonusView
from .models import SubmittableExercise, GeneratedExercise, Submission, FileSubmission

class MultipleSubmissionsListFilter(admin.SimpleListFilter):
    title = (u'Αποκρυψη παλαιων υποβολών')
    parameter_name = 'only_last'

    def lookups(self, request, model_admin):
        return (
            (True, u'Ναι'),
        )

    def queryset(self, request, queryset):
        if self.value():
            # TODO: Too slow approach. Will try to think something better.
            all_subm = list( queryset)
            users = set( sub.user for sub in all_subm)
            exercises = set( sub.exercise for sub in all_subm)

            last_submissions = [ ]
            for user in users:
                for exercise in exercises:
                    try:
                        subm = queryset.filter(user=user, exercise=exercise).latest('time_submitted')
                    except:
                        continue

                    last_submissions.append(subm)

            old_submissions = [ subm for subm in all_subm if subm not in last_submissions]

            for old_subm in old_submissions:
                queryset = queryset.exclude(
                    user=old_subm.user,
                    exercise=old_subm.exercise,
                    time_submitted=old_subm.time_submitted
                )

        return queryset


class FileSubmissionAdmin(admin.ModelAdmin):
    actions = ['download_zip']
    list_display = ('exercise', 'user', 'time_submitted' )
    list_filter = ('exercise__tag', MultipleSubmissionsListFilter, )

    ordering = ['-exercise__tag', 'user', '-time_submitted']

    def download_zip(self, request, queryset):
        from zipfile import ZipFile

        # Get the files from submissions
        files = [ os.path.join(settings.MEDIA_ROOT, subm.file.name)
                        for subm in queryset ]

        # Create the ZIP archive
        zip_path = '/tmp/file_submissions.zip'
        try:
            with ZipFile(zip_path, 'w') as zip_file:
                for f in files:
                    zip_file.write(filename=f, arcname=os.path.split(f)[1])
                zip_file.testzip()
        except Exception as e:
            self.message_user(request, 'Error: %s' % e, level=messages.ERROR)
            return

        # Send the response
        zip_file = open(zip_path, 'r')
        response = HttpResponse(zip_file, content_type='appliction/zip')
        response['Content-Disposition'] = 'attachment; filename=file_submissions.zip'
        return response

    download_zip.short_description = u"Κατεβασμα ZIP αρχείου με τις επιλεγμένες υποβολές"

admin.site.register(Submission)
admin.site.register(FileSubmission, FileSubmissionAdmin)
admin.site.register(SubmittableExercise)
admin.site.register(GeneratedExercise)

@admin.register(BonusLink)
class BonusLinkAdmin(admin.ModelAdmin):
    list_display = ('secret',)

@admin.register(BonusView)
class BonusViewAdmin(admin.ModelAdmin):
    list_display = ('link', 'user', 'date_viewed')
