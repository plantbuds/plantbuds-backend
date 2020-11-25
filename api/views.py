from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PbEncyclopedia, PlantProfile
from .serializers import EncyclopediaSerializer, UserSerializer, GroupSerializer, PlantProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EncyclopediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the encyclopedia to be viewed or edited
    """
    queryset = PbEncyclopedia.objects.all()
    serializer_class = EncyclopediaSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantProfileViewSet(viewsets.ModelViewSet):
    queryset = PlantProfile.objects.all()
    serializer_class = PlantProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Get a user's list of plant profiles
        """
        queryset = PlantProfile.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user=User.objects.get(username=username))
        return queryset

