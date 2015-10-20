from django.db import models
from embed_video.fields import EmbedVideoField

class Teacher(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

class Lecture(models.Model):
    tag = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    teachers = models.ManyToManyField(Teacher, related_name='lectures', blank=True)
    video = EmbedVideoField(null=True, blank=True)

    def __unicode__(self):
        return "%s : %s" % (self.tag, self.title)

class Slide(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(default='', blank=True)
    lecture = models.ForeignKey(Lecture, related_name='slides')

    def __unicode__(self):
        return "%s : %s" % (self.title, self.url)
