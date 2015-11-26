# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0008_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeapp',
            name='applied',
            field=models.CharField(default='RD', max_length=2, choices=[('RD', 'Regular Decision'), ('ED', 'Early Decision'), ('EA', 'Early Action'), ('PR', 'Priority'), ('RL', 'Rolling Admission')]),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='result',
            field=models.CharField(default='NA', max_length=2, choices=[('NA', 'Applied'), ('AC', 'Accepted'), ('RJ', 'Rejected')]),
        ),
        migrations.AlterField(
            model_name='senior',
            name='act',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat1600',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='sat2400',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
