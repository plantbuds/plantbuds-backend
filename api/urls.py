from django.urls import path

from . import views

urlpatterns = [
    path('encyclopedia/', views.encyclopedia, name='encyclopedia')
]