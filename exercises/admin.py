from django.contrib import admin
from .models import BonusLink, BonusView

from .models import SubmittableExercise, GeneratedExercise, Submission, FileSubmission

class MultipleSubmissionsListFilter(admin.SimpleListFilter):
    title = ('Multiple Submissions')
    parameter_name = 'only_last'

    def lookups(self, request, model_admin):
        return (
            (True, 'Latest'),
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
    list_display = ('exercise', 'user', 'time_submitted' )
    list_filter = ('exercise__tag', MultipleSubmissionsListFilter, )

    ordering = ['-exercise__tag', 'user', '-time_submitted']


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
