# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0004_auto_20160329_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='output',
            field=models.TextField(default='Empty'),
        ),
        migrations.AlterField(
            model_name='code',
            name='output_html',
            field=models.TextField(default='Empty'),
        ),
    ]
