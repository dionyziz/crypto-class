# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import exercises.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0009_generatedexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_submitted', models.DateTimeField()),
                ('score', models.SmallIntegerField(default=-1)),
                ('file', models.FileField(upload_to=exercises.models.exercise_save_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='submittableexercise',
            name='submissions',
        ),
        migrations.AddField(
            model_name='submission',
            name='exercise',
            field=models.ForeignKey(default=1, to='exercises.SubmittableExercise'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='generatedexercise',
            unique_together=set([('exercise', 'user')]),
        ),
        migrations.AddField(
            model_name='filesubmission',
            name='exercise',
            field=models.ForeignKey(to='exercises.SubmittableExercise'),
        ),
        migrations.AddField(
            model_name='filesubmission',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
