from rest_framework import serializers
from .models import PbEncyclopedia, PlantProfile
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
        fields = '__all__'
