from django.shortcuts import render

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


def list_shirts(request):
    shirts = Shirts.objects.filter(is_active = True)
    context = {
        'shirts':shirts
    }
    return render(request, 'shirts/list_shirts.html', context=context)