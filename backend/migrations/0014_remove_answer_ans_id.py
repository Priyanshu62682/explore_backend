# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-26 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_answer_answered_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='ans_id',
        ),
    ]