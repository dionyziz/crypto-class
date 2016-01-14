from django.db import models


class HttpsPassword(models.Model):
    password = models.TextField()
    filename = models.TextField()
