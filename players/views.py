from django.shortcuts import render

from players.models import Players
from players.forms import PlayersForm

# Create your views here.


def create_player(request):
    if request.method == 'GET':
        context = {
            'form': PlayersForm()
        }

        return render(request, 'players/player_create.html', context=context)

    elif request.method == 'POST':
        form = PlayersForm(request.POST)
        if form.is_valid():
            Players.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                height = form.cleaned_data['height'],
                position = form.cleaned_data['position'],
            )
            context = {
                'message': 'Jugador creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PlayersForm()
            }
        return render(request, 'players/player_create.html', context=context)


def list_players(request):
    if 'search' in request.GET:
        search = request.GET['search']
        players = Players.objects.filter(first_name__icontains=search)
    else:
        players = Players.objects.all()
    context = {
        'players':players,
    }
    return render(request, 'players/list_players.html', context=context)

