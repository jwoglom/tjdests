# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0009_auto_20151126_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='act',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='gpa',
            field=models.DecimalField(default=0.0, null=True, max_digits=4, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat1600',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat2400',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
