# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20151006_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittableexercise',
            name='statement_url',
            field=models.URLField(default=b''),
        ),
    ]
