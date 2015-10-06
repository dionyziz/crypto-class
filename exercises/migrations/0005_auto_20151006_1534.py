# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_submitted', models.DateTimeField()),
                ('answer', models.CharField(max_length=1025)),
                ('success', models.BooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GiftExercise',
        ),
        migrations.RemoveField(
            model_name='submittableexercise',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='submittableexercise',
            name='save_dir',
        ),
        migrations.RemoveField(
            model_name='submittableexercise',
            name='solutions',
        ),
        migrations.AlterField(
            model_name='submittableexercise',
            name='submissions',
            field=models.ManyToManyField(related_name='submissions', to='exercises.Submission', blank=True),
        ),
    ]
