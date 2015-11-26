# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0010_auto_20151126_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='act',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='senior',
            name='gpa',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat1600',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat2400',
            field=models.IntegerField(default=0),
        ),
    ]
