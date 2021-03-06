# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 21:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50, verbose_name='identifier')),
                ('service', models.CharField(choices=[('helmet', 'Helmet')], max_length=50, verbose_name='service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identities', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user identity',
                'verbose_name_plural': 'user identities',
            },
        ),
        migrations.AlterUniqueTogether(
            name='useridentity',
            unique_together=set([('user', 'service')]),
        ),
    ]
