# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import quilljs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='editor2',
            field=quilljs.fields.RichTextField(default='test'),
            preserve_default=False,
        ),
    ]
