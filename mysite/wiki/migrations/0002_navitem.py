# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=20)),
                ('redirect', models.CharField(max_length=63)),
                ('priority', models.SmallIntegerField()),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
    ]
