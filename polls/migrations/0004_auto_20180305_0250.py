# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180305_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(blank=True, to='polls.Post'),
        ),
    ]
