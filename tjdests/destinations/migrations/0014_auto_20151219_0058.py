# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0013_auto_20151126_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apexam',
            name='name',
            field=models.CharField(max_length=100, choices=[('Art History', 'Art History'), ('Music Theory', 'Music Theory'), ('Studio Art 2D', 'Studio Art 2D'), ('Studio Art 3D', 'Studio Art 3D'), ('Studio Art Drawing', 'Studio Art Drawing'), ('English Language', 'English Language'), ('English Literature', 'English Literature'), ('Comparative Govt', 'Comparative Govt'), ('European History', 'European History'), ('Human Geography', 'Human Geography'), ('Macroeconomics', 'Macroeconomics'), ('Microeconomics', 'Microeconomics'), ('Psychology', 'Psychology'), ('US Government/Politics', 'US Government/Politics'), ('US History', 'US History'), ('World History', 'World History'), ('Calculus AB', 'Calculus AB'), ('Calculus BC', 'Calculus BC'), ('Computer Science A', 'Computer Science A'), ('Statistics', 'Statistics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Environmental Science', 'Environmental Science'), ('Physics C E&M', 'Physics C E&M'), ('Physics C Mech', 'Physics C Mech'), ('Physics 1', 'Physics 1'), ('Physics 2', 'Physics 2'), ('Chinese', 'Chinese'), ('French', 'French'), ('German', 'German'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Latin', 'Latin'), ('Spanish Lang', 'Spanish Lang'), ('Spanish Lit', 'Spanish Lit')]),
        ),
    ]
