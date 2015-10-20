# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
        ('exercises', '0011_add_uploaded_filename_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittableexercise',
            name='lecture',
            field=models.ForeignKey(related_name='exercises', blank=True, to='lectures.Lecture', null=True),
        ),
    ]
