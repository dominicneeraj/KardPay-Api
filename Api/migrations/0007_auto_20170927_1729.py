# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_shopcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='brand',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
