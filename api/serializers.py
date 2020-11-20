from rest_framework import serializers
from .models import PbEncyclopedia
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EncyclopediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PbEncyclopedia
        fields = ['id', 'name', 'water', 'sun', 'propagation', 'hardiness', 'url']

class PlantProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlantProfile
        fields = ['id', 'plant_id', 'user_id', 'plant_name', 'nickname', 'photo', 'water_history', 'fertilize_history', 'repot_history', 'water_frequency', 'fertilize_frequency', 'repot_frequency', 'water_next_notif', 'fertilize_next_notif', 'repot_next_notif', 'notes']
