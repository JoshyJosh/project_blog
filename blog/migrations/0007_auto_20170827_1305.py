# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-27 11:05
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170827_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codepost',
            name='thumb',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='blog_thumbs', to='filer.Image'),
        ),
    ]