# Generated by Django 3.1.3 on 2020-12-03 21:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201202_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprofile',
            name='history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='plantprofile',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
