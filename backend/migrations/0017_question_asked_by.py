# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-27 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20161127_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asked_by',
            field=models.CharField(default='null', max_length=5000),
            preserve_default=False,
        ),
    ]
