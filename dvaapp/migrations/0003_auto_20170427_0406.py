# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 04:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0002_query_approximate'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='clustercodes',
            index_together=set([('clusters', 'searcher_index')]),
        ),
    ]
