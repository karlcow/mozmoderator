# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderate', '0006_mozillianprofile_is_nda_member'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_at']},
        ),
    ]