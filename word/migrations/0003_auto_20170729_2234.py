# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_auto_20170729_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='extended',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicaltranslation',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='desc',
            field=models.ManyToManyField(blank=True, to='word.Description'),
        ),
        migrations.AlterField(
            model_name='word',
            name='tags',
            field=models.ManyToManyField(blank=True, to='word.Tag'),
        ),
    ]