# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='compile_status',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='last_saved_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='memory_used',
            field=models.IntegerField(default=64),
        ),
        migrations.AddField(
            model_name='code',
            name='output',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='output_html',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='status',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='code',
            name='status_detail',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='code',
            name='time_used',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='code',
            name='user_input',
            field=models.TextField(null=True),
        ),
    ]
