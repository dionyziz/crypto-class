# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_submission_contains_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesubmission',
            name='uploaded_filename',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
