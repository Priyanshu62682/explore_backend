# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-20 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20161120_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answered_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='asked_by',
        ),
    ]