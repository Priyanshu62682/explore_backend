# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20161118_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expertise_area',
            old_name='city1',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ans_id',
        ),
    ]
