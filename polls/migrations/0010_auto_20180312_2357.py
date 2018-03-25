# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180312_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post_comment',
            field=models.ForeignKey(to='polls.Post'),
        ),
    ]
