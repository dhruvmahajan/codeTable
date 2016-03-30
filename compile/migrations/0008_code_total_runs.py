# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0007_auto_20160329_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='total_runs',
            field=models.IntegerField(default=0),
        ),
    ]
