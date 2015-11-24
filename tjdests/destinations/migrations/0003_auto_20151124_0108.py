# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_auto_20151122_0623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='verify_key',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='result',
            field=models.CharField(default='NA', max_length=2, choices=[('NA', 'Applied'), ('AT', 'Attending'), ('AC', 'Accepted'), ('RJ', 'Rejected')]),
        ),
    ]
