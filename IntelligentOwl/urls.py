from django.urls import path

from IntelligentOwl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game_creation', views.game_creation, name='game_creation'),
    path('team_editor', views.team_editor, name='team_editor'),
    path('team_browser', views.team_browser, name='team_browser')

]
