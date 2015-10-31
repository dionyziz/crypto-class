import os.path

from django.db import models
from django.db.models.query import EmptyQuerySet
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
from jsonfield import JSONField
from .registry import get_generator

class SubmittableExercise(models.Model):
    # e.g. "1.1", "3.5" etc.
    tag = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    lecture = models.ForeignKey('lectures.Lecture', related_name='exercises', blank=True, null=True)

    description = models.TextField(blank=True)
    statement_url = models.URLField(default='', blank=True)

    THEORETICAL = 'theoretical'
    AUTO_GRADING = 'autograding'
    type = models.CharField(max_length=20,
                            choices=(
                                (THEORETICAL, THEORETICAL),
                                (AUTO_GRADING, AUTO_GRADING),
                            ),
                            default=THEORETICAL
                            )
    deadline = models.DateTimeField()

    def __unicode__(self):
        return unicode("%s: %s" % (self.tag, self.title))

    def get_status(self, user):
        if not user.is_authenticated():
            return ''

        if self.type == SubmittableExercise.THEORETICAL:
            submissions = FileSubmission.objects.filter(exercise=self, user=user)
            if not submissions:
                return ''

            last_submission = submissions.order_by('-time_submitted')[0]

            if last_submission.score >= 0:
                return 'success'
            else:
                return 'active'
        else:
            submissions = Submission.objects.filter(exercise=self, user=user)
            if not submissions:
                return ''

            last_submission = submissions.order_by('-time_submitted')[0]

            if last_submission.is_solution:
                return 'success'
            else:
                return ''

    def is_submitted_by(self, user):
        if self.type == SubmittableExercise.THEORETICAL:
            return True if FileSubmission.objects.filter(exercise=self, user=user) else False
        else:
            return True if SubmittableExercise.objects.filter(exercise=self, user=user) else False

    def can_be_submitted(self):
        return True

    def get_generated(self, user):
        if user.is_authenticated():
            try:
                generated = GeneratedExercise.objects.get(user=user, exercise=self)
                return generated
            except GeneratedExercise.DoesNotExist:
                pass
        try:
            generator_class = get_generator(self.tag)
        except KeyError:
            return None

        generator = generator_class()
        metadata = generator.metadata
        generated = GeneratedExercise()
        generated.exercise = self
        generated.metadata = generator.metadata
        generated.message = generator.message

        if user.is_authenticated():
            generated.user = user
            generated.save()

        return generated

    def get_generated_metadata(self, user):
        generated = self.get_generated(user)
        if not generated:
            return None
        return generated.metadata

    def get_generated_message(self, user):
        generated = self.get_generated(user)
        if not generated:
            return None
        return generated.message

class GeneratedExercise(models.Model):
    """A SubmittableExercise with additional metadata and message generated for a specific user"""
    exercise = models.ForeignKey(SubmittableExercise)
    user = models.ForeignKey(User)
    metadata = JSONField()
    message = models.TextField()

    def __unicode__(self):
        return u"%s generated for %s" % (self.exercise.tag, self.user.username,)

    class Meta:
        unique_together = (("exercise", "user",),)

class Submission(models.Model):
    user = models.ForeignKey(User)
    time_submitted = models.DateTimeField()
    exercise = models.ForeignKey(SubmittableExercise)

    answer = models.CharField(max_length=1025)
    is_solution = models.BooleanField()

    def __unicode__(self):
        return u'[%s] %s (%s)' % (
                self.exercise.tag,
                self.user.username,
                self.time_submitted.strftime('%d/%m/%y %H:%M')
                )

def exercise_save_path(instance, filename):
    (_, file_ext) = os.path.splitext(filename)

    submissions = FileSubmission.objects.filter(
                    user=instance.user,
                    exercise=instance.exercise
                    )

    filename = '{0}_{1}_{2}{3}'.format(
            instance.exercise.tag,
            instance.user.username,
            len(submissions),
            file_ext
            )

    return 'submissions/exercise/{0}/{1}/{2}'.format(
                instance.exercise.tag,
                instance.user.username,
                filename
                )

class FileSubmission(models.Model):
    NOT_GRADED = -1

    user = models.ForeignKey(User)
    exercise = models.ForeignKey(SubmittableExercise)
    time_submitted = models.DateTimeField()

    score = models.SmallIntegerField(default=NOT_GRADED)
    file = models.FileField(upload_to=exercise_save_path)
    uploaded_filename = models.CharField(max_length=100)

    def __unicode__(self):
        return u'[%s] %s %s (%s)' % (
                self.exercise.tag,
                self.user.username,
                self.file.url,
                self.time_submitted.strftime('%d/%m/%y %H:%M')
                )

    def get_colored_status(self):
        """ This is used for changing row color (bootstrap) """
        if self.score == FileSubmission.NOT_GRADED:
            return "info"
        elif self.score == 0:
            return "danger"
        else:
            return "success"


class BonusLink(models.Model):
    """A bonus link that when accessed gives extra points to the student.
    Model specifies a secret that will be part of the url that the user has to guess."""
    secret = models.CharField(max_length=120)

    def __unicode__(self):
        return u'%s' % (self.secret,)

class BonusView(models.Model):
    user = models.ForeignKey(User)
    link = models.ForeignKey(BonusLink)
    date_viewed = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s view %s' % (self.user.username, self.link.secret)

