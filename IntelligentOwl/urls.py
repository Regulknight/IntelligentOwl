from django.urls import path

from IntelligentOwl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game_creation', views.game_creation, name='game_creation'),
    path('team_creation', views.team_creation, name='team_creation')
]
