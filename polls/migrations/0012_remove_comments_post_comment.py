# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180312_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post_comment',
        ),
    ]
