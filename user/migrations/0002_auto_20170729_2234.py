# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='proficiency',
            field=models.PositiveIntegerField(default=0),
        ),
    ]