from django.db import models

class Base64Quote(models.Model):
    quote = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.quote)

class Rot13Quote(models.Model):
    quote = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.quote)

class SubstitutionQuote(models.Model):
    quote = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.quote)

