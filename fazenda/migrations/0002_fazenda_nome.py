# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fazenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fazenda',
            name='nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]