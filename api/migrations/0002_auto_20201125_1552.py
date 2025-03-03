# Generated by Django 3.1.3 on 2020-11-25 23:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprofile',
            name='fertilize_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='plantprofile',
            name='repot_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='plantprofile',
            name='water_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
