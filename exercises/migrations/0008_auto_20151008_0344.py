# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_add_statement_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittableexercise',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='submittableexercise',
            name='statement_url',
            field=models.URLField(default=b'', blank=True),
        ),
    ]
