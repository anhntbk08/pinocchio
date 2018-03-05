# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0001_initial')
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionGrouping',
        ),
        migrations.AddField(
            model_name='questionorder',
            name='questionGrouping',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='peer_review.QuestionGrouping'),
        ),
    ]