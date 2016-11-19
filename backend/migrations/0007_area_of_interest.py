# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_question_asked_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='area_of_interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.appuser')),
            ],
        ),
    ]
