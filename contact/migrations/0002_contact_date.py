# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]