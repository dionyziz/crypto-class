# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.PositiveSmallIntegerField()),
                ('url', models.CharField(max_length=500)),
                ('solved_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GradedExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('solutions', models.ManyToManyField(related_name='solutions', to=settings.AUTH_USER_MODEL)),
                ('submissions', models.ManyToManyField(related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
