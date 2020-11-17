# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres import fields

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

class PlantProfile(models.Model):
    id = models.AutoField(primary_key=True)
    plant_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True,null=False)
    plant_name = models.TextField(blank=True, null=True) 
    nickname = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    water_history = fields.ArrayField(models.DateField(blank=True, null=True))
    fertilize_history = fields.ArrayField(models.DateField(blank=True, null=True))
    repot_history = fields.ArrayField(models.DateField(blank=True, null=True))
    water_frequency = models.IntegerField(blank=True, null=True) 
    fertilize_frequency = models.IntegerField(blank=True, null=True)
    repot_frequency = models.IntegerField(blank=True, null=True)
    water_next_notif = models.DateField(blank=True, null=True)
    fertilize_next_notif = models.DateField(blank=True, null=True) 
    repot_next_notif = models.DateField(blank=True, null=True)
    notes = fields.ArrayField(models.TextField(blank=True, null=True))

    def __str__(self):
        return self.plant_id

    class Meta:
        managed = False
        db_table = 'plant_Profile'
