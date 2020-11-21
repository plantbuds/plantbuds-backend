from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.db.utils import IntegrityError
from rest_framework import viewsets, permissions

from .models import PbEncyclopedia, UserProfile
from .serializers import EncyclopediaSerializer, UserSerializer, UserProfileSerializer, \
    SocialSerializer  # PlantProfileSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .users import validate_google_token
import requests


class UserProfileViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows user profiles to be viewed or edited
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    # POST /api/users/ with id_token to create a user
    def create(self, request, *args, **kwargs):

        # validate the google token
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['id_token']
            id_info = validate_google_token(token)
            if id_info is None:
                return Response(
                    {'errors': {'token': 'Invalid token'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {'errors': {'token': 'Token provided incorrectly'}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # get the user's google profile info
        token_info_url = 'https://oauth2.googleapis.com/tokeninfo?id_token=' + token
        response = requests.get(token_info_url)

        if response.status_code != requests.codes.ok:
            return Response(
                {'error': 'Couldn\'t retrieve google profile info'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        info = response.json()

        # add the user to the user_profile table
        email = info['email']
        username = email[:email.find('@')]
        try:
            user = UserProfile.objects.create(
                google_id=info['sub'],
                photo=info['picture'],
                username=username,
                email=info['email']
            )
            serializer = UserProfileSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {'error': 'user already exists in user profile table'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response(
                {'error': 'user could not be created'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    # POST /api/users/login/ with access_token
    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):

        if 'access_token' not in request.data.keys():
            return Response(
                {'error': 'access_token not provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        access_token = request.data['access_token']
        access_token_url = 'https://oauth2.googleapis.com/tokeninfo?access_token=' + access_token
        response = requests.get(access_token_url)

        if response.status_code != requests.codes.ok:
            return Response(
                {'error': 'access_token not valid'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # get the user by google_id
        try:
            user = UserProfile.objects.get(google_id=response.json()['sub'])
            serializer = UserProfileSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response(
                {'msg': 'user not found'},
                status=status.HTTP_200_OK,
            )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class EncyclopediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the encyclopedia to be viewed or edited
    """
    queryset = PbEncyclopedia.objects.all()
    serializer_class = EncyclopediaSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
class PlantProfile(viewsets.ModelViewSet):
    queryset = PlantProfile.objects.all()
    serializer_class = PlantProfileSerializer
    permission_classses = [permissions.IsAuthenticated]
"""
