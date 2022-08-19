from multiprocessing import context
from django.http import HttpResponse

def estudiante_de_coder(request):
    return render (request, 'estudiante_de_coder.html', context={})

def padre(request):
    return render (request, 'padre.html', context={})

def madre(request):
    return render (request, 'madre.html', context={})

def hermana(request):
    return render (request, 'hermana.html', context={})

def hermano(request):
    return render (request, 'hermano.html', context={})