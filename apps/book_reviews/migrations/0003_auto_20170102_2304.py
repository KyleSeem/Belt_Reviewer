# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0002_auto_20170102_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='book',
        ),
        migrations.AddField(
            model_name='reviewer',
            name='review',
            field=models.ForeignKey(default=9999, on_delete=django.db.models.deletion.CASCADE, to='book_reviews.Review'),
            preserve_default=False,
        ),
    ]