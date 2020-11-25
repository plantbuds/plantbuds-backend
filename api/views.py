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
        qs = self.queryset
        qs1 = qs.filter(user=self.request.user)

        return qs1
    """
    @action(detail=True, methods=['post'])
    def add(self, request):
        plant_list = PlantProfileViewSet.get_queryset()
        serializer = PlantProfileSerializer(plant_list, many=True)
        return Response(serializer.data)

    def plant_profile(self, request):
        if request.method == "GET":
            plant_list = PlantProfile.objects.all()
            serializer = PlantProfileSerializer(plant_list, many=True)
            return Response(serializer.data, safe=False)

    def create(self, request):
        if request.method == "POST":
            plant_list = PlantProfileViewSet.get_queryset()
            serializer = PlantProfileSerializer(plant_list, many=True)
            return Response(serializer.data, safe=False) 


# Return list of all encyclopedia entries (test function, not REST!!)
def encyclopedia(request):
    if request.method == "GET":
        plant_list = PbEncyclopedia.objects.all()
        serializer = EncyclopediaSerializer(plant_list, many=True)
        return JsonResponse(serializer.data, safe=False)

def plantprofile(request):
    if request.method == "GET":
        plant_list = PlantProfile.objects.all()
        serializer = PlantProfileSerializer(plant_list, many=True)
        return JsonResponse(serializer.data, safe=False)
"""

