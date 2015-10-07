from django.db import models
from django.db.models.query import EmptyQuerySet
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone

class Submission(models.Model):
    user = models.ForeignKey(User)
    time_submitted = models.DateTimeField()

    answer = models.CharField(max_length=1025)
    is_solution = models.BooleanField()

    def __unicode__(self):
        return u'%s: %s' % (self.user.username, self.time_submitted.strftime('%d/%m/%y %H:%M'))

class SubmittableExercise(models.Model):
    # e.g. "1.1", "3.5" etc.
    tag = models.CharField(max_length=10)
    title = models.CharField(max_length=150)

    description = models.TextField()
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

    submissions = models.ManyToManyField(Submission, related_name='submissions', blank=True)
    # Applicable to theory exercises (folder to save pdfs)
    # save_dir = models.FilePathField(upload_to=settings.UPLOAD_DIR, blank=True, max_length=500)

    def __unicode__(self):
        return unicode("%s: %s" % (self.tag, self.title))

    def is_solved_by_user(self, user):
        pass

    def can_be_submitted(self):
        return self.deadline >= timezone.now()

    def get_user_submissions(self, user):
        return self.submissions.filter(user=user).order_by('-time_submitted')

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

