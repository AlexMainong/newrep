# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
