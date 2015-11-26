from django.db import models

class RSAValues(models.Model):
    n = models.TextField()
    e = models.TextField()
    d = models.TextField()
