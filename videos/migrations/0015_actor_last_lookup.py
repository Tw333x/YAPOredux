# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20160622_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='last_lookup',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
