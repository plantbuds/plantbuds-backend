from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from .models import PbEncyclopedia
from .serializers import EncyclopediaSerializer, UserSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EncyclopediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the encyclopedia to be viewed or edited
    """
    queryset = PbEncyclopedia.objects.all()
    serializer_class = EncyclopediaSerializer
    permission_classes = [permissions.IsAuthenticated]
