# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 18:42
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0004_ipam_vlangroup_uniqueness'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlan',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vlan',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
