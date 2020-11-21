# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    google_id = models.TextField(blank=True, null=True, unique=True)
    photo = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True, unique=True)
    password = models.TextField(blank=True, null=True)
    email = models.TextField(null=True, unique=True)
    USDA_zone = models.TextField(blank=True, null=True)
    receive_water_notif = models.BooleanField(blank=True, null=True)
    receive_repot_notif = models.BooleanField(blank=True, null=True)
    receive_fertilizing_notif = models.BooleanField(blank=True, null=True)
    notif_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_profiles'


class PbEncyclopedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)  # This field type is a guess.
    sun = models.TextField(blank=True, null=True)  # This field type is a guess.
    propagation = models.TextField(blank=True, null=True)  # This field type is a guess.
    hardiness = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'pb_encyclopedia'
