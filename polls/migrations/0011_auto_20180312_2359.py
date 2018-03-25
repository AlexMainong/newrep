# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180312_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(null=True, to='polls.Post'),
        ),
    ]
