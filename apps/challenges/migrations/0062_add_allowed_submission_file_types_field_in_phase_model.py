# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-25 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0061_add_models_to_store_kubernetes_cluster_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="challengephase",
            name="allowed_submission_file_types",
            field=models.CharField(
                default=".json, .zip, .txt, .tsv, .gz, .csv, .h5, .npy",
                max_length=200,
            ),
        ),
    ]
