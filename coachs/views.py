from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
