# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesBuy',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=4)),
                ('amount', models.BigIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.Project')),
            ],
        ),
    ]
