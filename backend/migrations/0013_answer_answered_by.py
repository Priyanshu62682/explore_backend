# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20161122_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_by',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
