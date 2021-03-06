# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-13 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_preference',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='payments.PaymentPreference'),
        ),
    ]
