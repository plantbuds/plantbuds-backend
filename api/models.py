# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres import fields


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
    water = fields.ArrayField(models.TextField(blank=True, null=True))
    sun = fields.ArrayField(models.TextField(blank=True, null=True))
    propagation = fields.ArrayField(models.TextField(blank=True, null=True))
    hardiness = fields.ArrayField(models.TextField(blank=True, null=True))
    url = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    where_to_grow = fields.ArrayField(models.TextField(blank=True, null=True))
    img = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'pb_encyclopedia'


class PlantProfile(models.Model):
    id = models.AutoField(primary_key=True)
    encyclopedia = models.ForeignKey(PbEncyclopedia, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(UserProfile, models.SET_NULL, null=True)
    plant_name = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True, default="My Plant")
    photo = models.TextField(blank=True, null=True, default="https://i.imgur.com/4os1ZjY.png")
    water_history = fields.ArrayField(models.DateField(blank=True, null=True), blank=True, null=True)
    fertilize_history = fields.ArrayField(models.DateField(blank=True, null=True), blank=True, null=True)
    repot_history = fields.ArrayField(models.DateField(blank=True, null=True), blank=True, null=True)
    water_frequency = models.IntegerField(blank=True, null=True) 
    fertilize_frequency = models.IntegerField(blank=True, null=True)
    repot_frequency = models.IntegerField(blank=True, null=True)
    water_next_notif = models.DateField(blank=True, null=True)
    fertilize_next_notif = models.DateField(blank=True, null=True) 
    repot_next_notif = models.DateField(blank=True, null=True)
    notes = fields.ArrayField(models.TextField(blank=True, null=True), blank=True, null=True)

    def __str__(self):
        return self.plant_name

    class Meta:
        db_table = 'plant_profile'
