# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0011_auto_20151126_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='race',
            field=models.CharField(max_length=20, choices=[('White', 'White'), ('Asian', 'Asian'), ('Black', 'Black'), ('Hispanic', 'Hispanic'), ('Indian/AK Native', 'Indian/AK Native'), ('Multiracial', 'Multiracial')]),
        ),
    ]
