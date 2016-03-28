# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code_id', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('source_code', models.CharField(max_length=20000)),
                ('lang', models.CharField(choices=[('C', 'C'), ('CPP', 'CPP'), ('PYTHON', 'PYTHON')], default='C', max_length=20)),
                ('compiled_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
