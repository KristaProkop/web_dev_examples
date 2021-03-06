# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='accepter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepter', to='friends.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='friends.User'),
        ),
    ]
