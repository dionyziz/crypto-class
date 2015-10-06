# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusview',
            name='date_viewed',
            field=models.DateField(default=datetime.datetime(2015, 10, 6, 11, 59, 51, 422275, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
