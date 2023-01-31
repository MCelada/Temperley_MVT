from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import DeleteView
from coachs.models import Coachs
from coachs.forms import CoachsForm

# Create your views here.


def create_coach(request):
    if request.method == 'GET':
        context = {
            'form': CoachsForm()
        }

        return render(request, 'coachs/create_coach.html', context=context)

    elif request.method == 'POST':
        form = CoachsForm(request.POST, request.FILES)
        if form.is_valid():
            Coachs.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                period = form.cleaned_data['period'],
            )
            context = {
                'message': 'DT creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': CoachsForm()
            }
        return render(request, 'coachs/create_coach.html', context=context)

@login_required
def list_coachs(request):
    coachs = Coachs.objects.filter(is_active = True)
    context = {
        'coachs':coachs
    }
    return render(request, 'coachs/list_coachs.html', context=context)


def update_coach(request, pk):
    coach = Coachs.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': CoachsForm(
                initial={
                    'first_name':coach.first_name,
                    'last_name':coach.last_name,
                    'age':coach.age,
                    'period':coach.period,
                }
            )
        }

        return render(request, 'coachs/update_coach.html', context=context)

    elif request.method == 'POST':
        form = CoachsForm(request.POST)
        if form.is_valid():
                coach.first_name = form.cleaned_data['first_name']
                coach.last_name = form.cleaned_data['last_name']
                coach.age = form.cleaned_data['age']
                coach.period = form.cleaned_data['period']
                coach.save()
            
                context = {
                    'message': 'Director Tecnico Actualizado con exito!'
                }
        else:
            context = {
                'form_errors': form.errors,
                'form': CoachsForm()
            }
        return render(request, 'coachs/update_coach.html', context=context)


class CoachDeleteView(DeleteView):
    model = Coachs
    template_name = 'coachs/delete_coach.html'
    success_url = '/coachs/list-coachs'
