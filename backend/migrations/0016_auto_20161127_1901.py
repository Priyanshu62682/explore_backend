# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-27 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_merge_20161126_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='asked_on',
            field=models.DateField(auto_now=True),
        ),
    ]
