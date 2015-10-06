# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittableExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('save_dir', models.FilePathField()),
                ('solutions', models.ManyToManyField(related_name='solutions', to=settings.AUTH_USER_MODEL, blank=True)),
                ('submissions', models.ManyToManyField(related_name='submissions', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gradedexercise',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='gradedexercise',
            name='submissions',
        ),
        migrations.DeleteModel(
            name='GradedExercise',
        ),
    ]
