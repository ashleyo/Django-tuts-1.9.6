# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_userfileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfileupload',
            name='name',
        ),
    ]
