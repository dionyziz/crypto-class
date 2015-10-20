# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='file',
        ),
        migrations.AddField(
            model_name='slide',
            name='url',
            field=models.URLField(default=b'', blank=True),
        ),
    ]
