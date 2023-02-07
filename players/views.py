from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from players.models import Players
from players.forms import PlayersForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

def create_player(request):
    if request.method == 'GET':
        context = {
            'form': PlayersForm()
        }
        return render(request, 'players/player_create.html', context=context)

    elif request.method == 'POST':
        form = PlayersForm(request.POST, request.FILES)
        if form.is_valid():
            Players.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                height = form.cleaned_data['height'],
                position = form.cleaned_data['position'],
                image = form.cleaned_data['image'],
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
    

@login_required
def list_players(request):
    if 'search' in request.GET:
        search = request.GET['search']
        players = Players.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
    else:
        players = Players.objects.all()
    context = {
        'players':players,
    }
    return render(request, 'players/list_players.html', context=context)

def update_player(request, pk): 
    player = Players.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': PlayersForm(
                initial={
                    'first_name':player.first_name,
                    'last_name':player.last_name,
                    'age':player.age,
                    'height':player.height,
                    'position':player.position,
                    'image':player.image,
                }
            )
        }

        return render(request, 'players/player_update.html', context=context)

    elif request.method == 'POST':
        form = PlayersForm(request.POST, request.FILES)
        if form.is_valid():
                player.first_name = form.cleaned_data['first_name']
                player.last_name = form.cleaned_data['last_name']
                player.age = form.cleaned_data['age']
                player.height = form.cleaned_data['height']
                player.position = form.cleaned_data['position']
                player.image = form.cleaned_data['image']
                player.save()
            
                context = {
                    'message': 'Jugador Actualizado exitosamente'
                }
        else:
            context = {
                'form_errors': form.errors,
                'form': PlayersForm()
            }
        return render(request, 'players/player_update.html', context=context)


class PlayerDeleteView(DeleteView):
    model = Players
    template_name = 'players/player_delete.html'
    success_url = '/players/list-players'