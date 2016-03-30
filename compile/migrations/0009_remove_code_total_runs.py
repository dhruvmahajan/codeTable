# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0008_code_total_runs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='total_runs',
        ),
    ]
