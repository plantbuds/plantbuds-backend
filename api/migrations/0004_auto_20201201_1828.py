# Generated by Django 3.1.3 on 2020-12-02 02:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201201_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprofile',
            name='notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
