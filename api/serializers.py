from rest_framework import serializers
from .models import PbEncyclopedia, UserProfile, PlantProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'auth_user', 'photo', 'username', 'email', 'USDA_zone',
                  'receive_water_notif', 'receive_repot_notif', 'receive_fertilizing_notif', 'notif_time']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_staff']


class EncyclopediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PbEncyclopedia
        fields = '__all__'


class PlantProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlantProfile
        fields = '__all__'


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    id_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
