# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0008_auto_20151008_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metadata', jsonfield.fields.JSONField()),
                ('message', models.TextField()),
                ('exercise', models.ForeignKey(to='exercises.SubmittableExercise')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
