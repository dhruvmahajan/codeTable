# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0003_code_stderr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='source_code',
            field=models.TextField(max_length=20000),
        ),
    ]
