# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_auto_20170923_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
