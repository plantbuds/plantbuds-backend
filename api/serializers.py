from rest_framework import serializers
from .models import PbEncyclopedia
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email']


class EncyclopediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PbEncyclopedia
        fields = ['id', 'name', 'water', 'sun', 'propagation', 'hardiness', 'url']


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
