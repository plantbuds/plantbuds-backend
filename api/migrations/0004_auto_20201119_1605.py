# Generated by Django 3.1.3 on 2020-11-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201119_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]
