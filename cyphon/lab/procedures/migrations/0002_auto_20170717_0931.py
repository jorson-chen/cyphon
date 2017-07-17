# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 13:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='package',
            field=models.CharField(choices=[('geoip', 'geoip'), ('language', 'language'), ('procedures', 'procedures'), ('sentiment', 'sentiment')], max_length=32, validators=[django.core.validators.RegexValidator('[a-zA-Z_][a-zA-Z0-9_]*', 'Not a valid Python identifier')]),
        ),
    ]
