# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20171221_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
