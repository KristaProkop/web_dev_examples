# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_key', models.TextField()),
                ('consumer_secret', models.TextField()),
                ('access_token', models.TextField()),
                ('access_token_secret', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
