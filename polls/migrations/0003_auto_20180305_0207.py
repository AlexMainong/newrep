# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='post_comment',
        ),
    ]
