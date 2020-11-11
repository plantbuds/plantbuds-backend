from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from .models import PbEncyclopedia
from .serializers import EncyclopediaSerializer, UserSerializer, GroupSerializer


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


# Return list of all encyclopedia entries (test function, not REST!!)
def encyclopedia(request):
    if request.method == "GET":
        plant_list = PbEncyclopedia.objects.all()
        serializer = EncyclopediaSerializer(plant_list, many=True)
        return JsonResponse(serializer.data, safe=False)
