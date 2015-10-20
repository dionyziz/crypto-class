# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0004_auto_20151020_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='teachers',
            field=models.ManyToManyField(related_name='lectures', to='lectures.Teacher', blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True, blank=True),
        ),
    ]
