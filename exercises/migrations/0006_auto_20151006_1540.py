# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20151006_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='success',
            new_name='is_solution',
        ),
    ]
