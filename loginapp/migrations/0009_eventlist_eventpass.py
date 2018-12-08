# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-08 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_auto_20181201_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('event1', models.TextField(default=0)),
                ('event2', models.TextField(default=0)),
                ('event3', models.TextField(default=0)),
                ('event4', models.TextField(default=0)),
                ('event5', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='eventpass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('pass1', models.TextField(default=0)),
                ('pass2', models.TextField(default=0)),
                ('pass3', models.TextField(default=0)),
                ('pass4', models.TextField(default=0)),
                ('pass5', models.TextField(default=0)),
            ],
        ),
    ]
