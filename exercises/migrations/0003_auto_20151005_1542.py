# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20151005_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittableexercise',
            name='type',
            field=models.CharField(default=b'theoretical', max_length=20, choices=[(b'theoretical', b'theoretical'), (b'autograding', b'autograding')]),
        ),
        migrations.AlterField(
            model_name='submittableexercise',
            name='save_dir',
            field=models.FilePathField(max_length=500, blank=True),
        ),
    ]
