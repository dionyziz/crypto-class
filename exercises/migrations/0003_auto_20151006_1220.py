# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_bonusview_date_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusview',
            name='date_viewed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
