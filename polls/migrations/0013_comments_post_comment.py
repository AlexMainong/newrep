# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_remove_comments_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(to='polls.Post', null=True),
        ),
    ]
