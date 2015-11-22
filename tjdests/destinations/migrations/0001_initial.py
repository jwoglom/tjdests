# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APExam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, choices=[('Art History', 'Art History'), ('Music Theory', 'Music Theory'), ('Studio Art 2D', 'Studio Art 2D'), ('Studio Art 3D', 'Studio Art 3D'), ('Studio Art Drawing', 'Studio Art Drawing'), ('Lang', 'Lang'), ('Lit', 'Lit'), ('Comparative Govt', 'Comparative Govt'), ('European History', 'European History'), ('Human Geography', 'Human Geography'), ('Macroeconomics', 'Macroeconomics'), ('Microeconomics', 'Microeconomics'), ('Psychology', 'Psychology'), ('US Government', 'US Government'), ('US History', 'US History'), ('World History', 'World History'), ('Calculus AB', 'Calculus AB'), ('Calculus BC', 'Calculus BC'), ('Comp Sci A', 'Comp Sci A'), ('Comp Sci Principles', 'Comp Sci Principles'), ('Statistics', 'Statistics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Environmental Science', 'Environmental Science'), ('Physics C E&M', 'Physics C E&M'), ('Physics C Mech', 'Physics C Mech'), ('Physics 1', 'Physics 1'), ('Physics 2', 'Physics 2'), ('Chinese', 'Chinese'), ('French', 'French'), ('German', 'German'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Latin', 'Latin'), ('Spanish Lang', 'Spanish Lang'), ('Spanish Lit', 'Spanish Lit')])),
                ('score', models.IntegerField()),
                ('year', models.IntegerField()),
                ('took_class', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('ceeb', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program', models.CharField(max_length=250)),
                ('attending', models.BooleanField()),
                ('applied', models.CharField(default='RD', max_length=2, choices=[('RD', 'Regular Decision'), ('ED', 'Early Decision'), ('EA', 'Early Action'), ('PR', 'Priority')])),
                ('result', models.CharField(default='NA', max_length=2, choices=[('RD', 'Regular Decision'), ('ED', 'Early Decision'), ('EA', 'Early Action'), ('PR', 'Priority')])),
                ('submitted', models.DateField(blank=True)),
                ('notified', models.DateField(blank=True)),
                ('legacy', models.BooleanField(default=False)),
                ('interview', models.BooleanField(default=False)),
                ('recruited', models.CharField(max_length=100)),
                ('supplement', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=1000)),
                ('college', models.ForeignKey(to='destinations.College')),
            ],
        ),
        migrations.CreateModel(
            name='SAT2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, choices=[('Literature', 'Literature'), ('US History', 'US History'), ('World History', 'World History'), ('Math Level 1', 'Math Level 1'), ('Math Level 2', 'Math Level 2'), ('Biology/EM', 'Biology/EM'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('French', 'French'), ('French Listening', 'French Listening'), ('German', 'German'), ('German Listening', 'German Listening'), ('Spanish', 'Spanish'), ('Spanish Listening', 'Spanish Listening'), ('Modern Hebrew', 'Modern Hebrew'), ('Italian', 'Italian'), ('Latin', 'Latin'), ('Chinese Listening', 'Chinese Listening'), ('Japanese Listening', 'Japanese Listening'), ('Korean Listening', 'Korean Listening')])),
                ('score', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('race', models.CharField(max_length=20)),
                ('hispanic', models.BooleanField()),
                ('international', models.BooleanField()),
                ('gpa', models.DecimalField(max_digits=4, decimal_places=3)),
                ('sat2400', models.IntegerField()),
                ('sat1600', models.IntegerField()),
                ('act', models.IntegerField()),
                ('honors', models.CharField(max_length=1000)),
                ('colleges', models.ManyToManyField(to='destinations.College', through='destinations.CollegeApp')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('senior', models.OneToOneField(null=True, to='destinations.Senior')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sat2',
            name='senior',
            field=models.ForeignKey(to='destinations.Senior'),
        ),
        migrations.AddField(
            model_name='collegeapp',
            name='senior',
            field=models.ForeignKey(to='destinations.Senior'),
        ),
        migrations.AddField(
            model_name='apexam',
            name='senior',
            field=models.ForeignKey(to='destinations.Senior'),
        ),
    ]
