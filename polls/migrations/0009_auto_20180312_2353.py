# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0008_comments_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 20, 53, 28, 187296, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_from',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
