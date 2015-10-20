# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0005_auto_20151020_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='tag',
            field=models.IntegerField(),
        ),
    ]
