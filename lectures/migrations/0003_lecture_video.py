# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20151020_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
