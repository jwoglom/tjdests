# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0006_auto_20151124_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeapp',
            name='notified',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='submitted',
            field=models.DateField(null=True, blank=True),
        ),
    ]
