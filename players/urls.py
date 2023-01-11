from django.urls import path

from players.views import create_player, list_players

urlpatterns = [
    path('create_player/', create_player),
    path('list-players/', list_players),
]