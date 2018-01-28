# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-12 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名称', max_length=30, verbose_name='名称')),
                ('desc', models.CharField(help_text='简介', max_length=100, verbose_name='简介')),
                ('image', models.ImageField(blank=True, help_text='图片', null=True, upload_to='base/friendlink/image/%y/%m', verbose_name='图片')),
                ('url', models.URLField(help_text='链接', verbose_name='链接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '自定义导航',
                'verbose_name_plural': '自定义导航列表',
            },
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='navigations',
            field=models.ForeignKey(blank=True, help_text='自定义导航', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.NavigationLink', verbose_name='自定义导航'),
        ),
    ]