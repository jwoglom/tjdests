# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_auto_20151124_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='honors',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
