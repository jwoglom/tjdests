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
                ('score', models.IntegerField()),
                ('year', models.IntegerField()),
                ('took_class', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='APTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
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
                ('applied', models.CharField(default=b'RD', max_length=2, choices=[(b'RD', b'Regular Decision'), (b'ED', b'Early Decision'), (b'EA', b'Early Action'), (b'PR', b'Priority')])),
                ('result', models.CharField(default=b'NA', max_length=2, choices=[(b'RD', b'Regular Decision'), (b'ED', b'Early Decision'), (b'EA', b'Early Action'), (b'PR', b'Priority')])),
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
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('race', models.CharField(max_length=20)),
                ('hispanic', models.BooleanField()),
                ('international', models.BooleanField()),
                ('gpa', models.DecimalField(max_digits=4, decimal_places=3)),
                ('sat2400', models.IntegerField()),
                ('sat1600', models.IntegerField()),
                ('act', models.IntegerField()),
                ('honors', models.CharField(max_length=1000)),
                ('aps', models.ManyToManyField(to='destinations.APTest', through='destinations.APExam')),
                ('colleges', models.ManyToManyField(to='destinations.College', through='destinations.CollegeApp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='collegeapp',
            name='user',
            field=models.ForeignKey(to='destinations.User'),
        ),
        migrations.AddField(
            model_name='apexam',
            name='aptest',
            field=models.ForeignKey(to='destinations.APTest'),
        ),
        migrations.AddField(
            model_name='apexam',
            name='user',
            field=models.ForeignKey(to='destinations.User'),
        ),
    ]
