from django.db import models
from django.contrib.auth.models import User

class BonusLink(models.Model):
    """A bonus link that when accessed gives extra points to the student.
    Model specifies a secret that will be part of the url that the user has to guess."""
    secret = models.CharField(max_length=120)

class BonusView(models.Model):
    user = models.ForeignKey(User)
    link = models.ForeignKey(BonusLink)
    date_viewed = models.DateField(auto_now_add=True)
