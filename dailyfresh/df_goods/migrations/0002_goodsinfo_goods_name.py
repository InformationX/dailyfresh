# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-24 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='商品简称'),
        ),
    ]