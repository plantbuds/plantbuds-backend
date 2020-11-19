from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions

from server.settings import GOOGLE_CLIENT_ID
from .models import PbEncyclopedia
from .serializers import EncyclopediaSerializer, UserSerializer, SocialSerializer, PlantProfileSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests

from requests.exceptions import HTTPError

from social_django.utils import psa


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


class PlantProfile(viewsets.ModelViewSet):
    queryset = PlantProfile.objects.all()
    serializer_class = PlantProfileSerializer
    permission_classses = [permissions.IsAuthenticated]


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
def exchange_token(request):
    serializer = SocialSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        try:
            token = serializer.validated_data['access_token']
            idinfo = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                GOOGLE_CLIENT_ID,
            )
            userid = idinfo['sub']
            print(f'user id: {userid}')

        except ValueError:
            return Response(
                {'errors': {'token': 'Invalid token'}},
                status=status.HTTP_400_BAD_REQUEST,
            )

    """
    serializer = SocialSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        try:
            nfe = settings.NON_FIELD_ERRORS_KEY
        except AttributeError:
            nfe = 'non_field_errors'

        try:
            user = google.do_auth(serializer.validated_data['access_token'])
        except HTTPError as e:
            return Response(
                {'errors': {
                    'token': 'Invalid token',
                    'detail': str(e),
                }},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response(
                    {'errors': {nfe: 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        else:
            return Response(
                {'errors': {nfe: 'Authentication failed'}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        """
