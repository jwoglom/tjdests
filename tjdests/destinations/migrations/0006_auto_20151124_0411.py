# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0005_auto_20151124_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeapp',
            name='notified',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='submitted',
            field=models.DateField(null=True),
        ),
    ]
