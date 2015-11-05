# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0006_auto_20151020_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='video_is_public',
            field=models.BooleanField(default=False, verbose_name=b'Video is public'),
        ),
    ]
