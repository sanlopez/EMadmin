# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_proj', '0017_auto_20171021_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='multiple_backup',
            field=models.BooleanField(default=False),
        ),
    ]
