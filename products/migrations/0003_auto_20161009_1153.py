# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161007_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
