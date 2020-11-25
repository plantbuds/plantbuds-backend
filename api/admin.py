from django.contrib import admin
from .models import PbEncyclopedia, PlantProfile, UserProfile

# Register your models here.
admin.site.register(PbEncyclopedia)
admin.site.register(PlantProfile)
admin.site.register(UserProfile)
