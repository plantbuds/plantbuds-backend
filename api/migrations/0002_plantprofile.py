# Generated by Django 3.1.3 on 2020-11-21 05:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plant_id', models.IntegerField(blank=True, null=True)),
                ('plant_name', models.TextField(blank=True, null=True)),
                ('nickname', models.TextField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
                ('water_history', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), size=None)),
                ('fertilize_history', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), size=None)),
                ('repot_history', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, null=True), size=None)),
                ('water_frequency', models.IntegerField(blank=True, null=True)),
                ('fertilize_frequency', models.IntegerField(blank=True, null=True)),
                ('repot_frequency', models.IntegerField(blank=True, null=True)),
                ('water_next_notif', models.DateField(blank=True, null=True)),
                ('fertilize_next_notif', models.DateField(blank=True, null=True)),
                ('repot_next_notif', models.DateField(blank=True, null=True)),
                ('notes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=None)),
            ],
            options={
                'db_table': 'plant_profile',
                'managed': False,
            },
        ),
    ]
