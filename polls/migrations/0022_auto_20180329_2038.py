# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0021_auto_20180328_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislike',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='post_like', blank=True),
        ),
        migrations.DeleteModel(
            name='LikeDislike',
        ),
    ]
