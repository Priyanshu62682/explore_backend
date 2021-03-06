# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='ans_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='answers',
            name='validity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questions',
            name='ans_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='q_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questions',
            name='status',
            field=models.IntegerField(),
        ),
    ]
