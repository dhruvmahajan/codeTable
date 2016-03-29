# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0006_auto_20160329_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='code',
            options={'ordering': ('-compiled_on',)},
        ),
        migrations.AlterField(
            model_name='code',
            name='source_code',
            field=models.TextField(),
        ),
    ]
