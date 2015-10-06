# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151004_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='first name', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='last name', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.CharField(max_length=120),
        ),
    ]
