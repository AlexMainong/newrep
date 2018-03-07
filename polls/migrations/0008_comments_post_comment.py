# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_comments_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(blank=True, default=0, to='polls.Post'),
            preserve_default=False,
        ),
    ]
