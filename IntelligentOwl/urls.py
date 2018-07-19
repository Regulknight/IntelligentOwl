from django.urls import path

from IntelligentOwl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games', views.game_browser, name='game_browser'),
    path('games/new', views.game_creation, name='game_creation'),
    path('games/<int:game_id>/', views.game_details, name='game_details'),
    path('teams/<int:team_id>/', views.team_details, name='team_details'),
    path('teams', views.team_browser, name='team_browser'),
    path('teams/new', views.team_new, name='team_creation'),
    path('game_conduction', views.game_conduction, name='game_conduction'),
    path('overall_rating', views.overall_rating, name='overall_rating')
]
