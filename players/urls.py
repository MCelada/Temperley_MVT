from django.urls import path

from players.views import create_player, list_players, update_player, PlayerDeleteView

urlpatterns = [
    path('create_player/', create_player),
    path('list-players/', list_players, name = 'list_players'),
    path('update_player/<int:pk>/', update_player),
    path('delete_player/<int:pk>/', PlayerDeleteView.as_view(template_name='players/player_delete.html'), name='player_delete'),
]