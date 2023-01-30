from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import DeleteView
from shirts.models import Shirts
from shirts.forms import ShirtsForm

# Create your views here.


def create_shirt(request):
    if request.method == 'GET':
        context = {
            'form': ShirtsForm()
        }

        return render(request, 'shirts/create_shirt.html', context=context)

    elif request.method == 'POST':
        form = ShirtsForm(request.POST)
        if form.is_valid():
            Shirts.objects.create(
                maker = form.cleaned_data['maker'],
                season = form.cleaned_data['season'],
            )
            context = {
                'message': 'Camiseta creada exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ShirtsForm()
            }
        return render(request, 'shirts/create_shirt.html', context=context)


@login_required
def list_shirts(request):
    shirts = Shirts.objects.filter(is_active = True)
    context = {
        'shirts':shirts
    }
    return render(request, 'shirts/list_shirts.html', context=context)


def update_shirt(request, pk):
    shirt = Shirts.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': ShirtsForm(
                initial={
                    'maker':shirt.maker,
                    'season':shirt.season,
                }
            )
        }

        return render(request, 'shirts/update_shirt.html', context=context)

    elif request.method == 'POST':
        form = ShirtsForm(request.POST)
        if form.is_valid():
                shirt.maker = form.cleaned_data['maker']
                shirt.season = form.cleaned_data['season']
                shirt.save()
            
                context = {
                    'message': 'Camiseta actualizada con exito!'
                }
        else:
            context = {
                'form_errors': form.errors,
                'form': ShirtsForm()
            }
        return render(request, 'shirts/update_shirt.html', context=context)


class ShirtDeleteView(DeleteView):
    model = Shirts
    template_name = 'shirts/delete_shirt.html'
    success_url = '/shirts/list-shirts/'
       