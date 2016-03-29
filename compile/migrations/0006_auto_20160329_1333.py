# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0005_auto_20160329_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='output',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='output_html',
            field=models.TextField(null=True),
        ),
    ]
