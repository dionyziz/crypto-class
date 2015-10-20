# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_lecture_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='teachers',
            field=models.ManyToManyField(related_name='lectures', null=True, to='lectures.Teacher', blank=True),
        ),
    ]
