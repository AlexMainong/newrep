# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20180326_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=140),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(default='', blank=True),
        ),
    ]
