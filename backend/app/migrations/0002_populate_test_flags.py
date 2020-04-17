# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-09 18:22
from __future__ import unicode_literals

from django.db import migrations, models


def add_flags(apps, schema_editor):
    flags = [
        ['turn-the-thing-on', 'This flag turns the thing on.'],
        ['prevent-the-broken-thing', 'This flag fixes the broken thing.'],
        ['test-1', 'Just the first test flag.'],
        ['do-nothing', 'It does not matter if this flag is on or off.'],
        ['broken-fix', 'This flag turns on a broken fix that causes more problems.'],
        ['dev-ops-flag', 'Developer only flag to help things.'],
        ['ping-slack', 'This flag turns on the ability for errors to go to slack.'],
        ['toggle-the-title', 'This flag turns the text from one thing to another.'],
        ['test-2', 'The second test flag.'],
        ['add-new-small-feature', 'A quick new feature.'],
        ['add-new-major-feature', 'A big initiative feature that took a long time to finish.'],
        ['no-more-ideas', 'This flag is cause I needed one more.'],
        ['turn-the-other-thing-on', 'This flag turns the other thing on.'],
        ['turn-the-old-thing-off', 'This flag turns the off an old thing.'],
        ['announcement-banner', 'This flag turns on an announcement banner.'],
        ['experimental-feature', 'Something we just wanted to try to see if it worked.'],
        ['add-another-major-new-feature', 'Another big initiative.'],
        ['do-not-delete-this-flag', 'Does a thing that we will need to maintain forever.'],
    ]
    i = 1
    for flag in flags:
        FeatureFlag = apps.get_model("app", "FeatureFlag")
        ff = FeatureFlag()
        enabled = i % 2 == 0 or i % 5 != 0
        deleted = i % 3 == 0
        long_term = i % 4 == 0
        ff.name = flag[0]
        ff.description = flag[1]
        ff.enabled = enabled and not deleted
        ff.deleted = deleted and not enabled and not long_term
        ff.long_term = long_term and not deleted
        ff.save()
        i = i + 1


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_flags),
    ]