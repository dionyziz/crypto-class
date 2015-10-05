from django.db import models

from django.db.models.query import EmptyQuerySet
from django.contrib.auth.models import User

class SubmittableExercise(models.Model):
    # e.g. "1.1", "3.5" etc.
    tag = models.CharField(max_length=10)

    title = models.CharField(max_length=150)
    description = models.TextField()

    THEORETICAL = 'theoretical'
    AUTO_GRADING = 'autograding'
    type = models.CharField(max_length=20,
                            choices=(
                                (THEORETICAL, THEORETICAL),
                                (AUTO_GRADING, AUTO_GRADING),
                            ),
                            default=THEORETICAL
                            )

    pub_date = models.DateTimeField()
    deadline = models.DateTimeField()

    submissions = models.ManyToManyField(User, related_name='submissions', blank=True)
    solutions = models.ManyToManyField(User, related_name='solutions', blank=True)

    # Applicable to theory exercises (folder to save pdfs)
    save_dir = models.FilePathField(max_length=500, blank=True, null=False)

    def __unicode__(self):
        return unicode("%s: %s" % (self.tag, self.title))

    def is_solved_by_user(self, user):
        user_solution = self.solutions.objects.filter(username=user.username)
        return not isinstance(user_solution, EmptyQuerySet)

    def user_submitions(self, user):
        return self.submittions.objects.filter(username=user.username)


class GiftExercise(models.Model):
    tag = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=500)

    solved_by = models.IntegerField()

