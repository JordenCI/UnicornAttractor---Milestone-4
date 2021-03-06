# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 14:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bug',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bug',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
