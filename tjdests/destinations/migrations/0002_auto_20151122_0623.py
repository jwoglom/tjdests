# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='college',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='collegeapp',
            name='deferred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collegeapp',
            name='waitlisted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='comments',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='recruited',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='result',
            field=models.CharField(default='NA', max_length=2, choices=[('NA', 'Applied'), ('AT', 'Attending'), ('AC', 'Accepted'), ('RJ', 'Rejected'), ('WL', 'Waitlisted'), ('DF', 'Deferred')]),
        ),
        migrations.AlterField(
            model_name='collegeapp',
            name='supplement',
            field=models.CharField(max_length=100, blank=True),
        ),
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
