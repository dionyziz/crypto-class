# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_generatedexercise'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='generatedexercise',
            unique_together=set([('exercise', 'user')]),
        ),
    ]
