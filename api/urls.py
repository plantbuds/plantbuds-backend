from django.urls import path

from . import views

urlpatterns = [
    path('encyclopedia/', views.EncyclopediaViewSet, name='encyclopedia'),
    path('plantprofile/', views.PlantProfileViewSet, name='plantprofile')
]
