# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_poststatistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(max_length=140),
        ),
    ]
