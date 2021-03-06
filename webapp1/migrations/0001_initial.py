# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 18:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('emp_id', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('phone_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')])),
            ],
        ),
    ]
