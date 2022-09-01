from datetime import date
from socket import TCP_NODELAY
from django.shortcuts import render
from familiares.models import Familiares

def new_fliar(request):
    new_fliar = Familiares.objects.create(name = 'Angel Gabriel', last_name = 'Masitti', age = '62', birth = '1960-08-13', date = date)
    context = {
        'new_fliar':new_fliar
    }
    return render(request, 'new_fliar.html', context=context)

