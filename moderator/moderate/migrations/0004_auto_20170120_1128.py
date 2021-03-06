# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-20 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations

from moderator.moderate.mozillians import BadStatusCode, MozilliansClient, ResourceDoesNotExist


def forwards(apps, schema_editor):
    """Forwards method.

    Sync with mozillians.org to fix avatar url.
    """
    User = apps.get_model('auth', 'User')
    mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                         settings.MOZILLIANS_API_KEY)
    for user in User.objects.all():

        try:
            mozillian_user = mozillians_client.lookup_user({'email': user.email})
        except (BadStatusCode, ResourceDoesNotExist):
            continue

        if mozillian_user['photo']['privacy'] == 'Public':
            user.userprofile.avatar_url = mozillian_user['photo']['value']
        else:
            user.userprofile.avatar_url = ''
        user.userprofile.save()


def backwards(apps, schema_editor):
    """Backwards method.

    Do nothing please.
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('moderate', '0003_auto_20170118_1536'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
