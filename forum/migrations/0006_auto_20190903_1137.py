# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-03 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_forumpost_comment_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='desc',
            new_name='description',
        ),
    ]