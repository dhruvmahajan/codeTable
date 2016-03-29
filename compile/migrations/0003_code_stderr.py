# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0002_auto_20160329_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='stderr',
            field=models.TextField(null=True),
        ),
    ]
