# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_remove_page_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitsCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
            ],
        ),
    ]