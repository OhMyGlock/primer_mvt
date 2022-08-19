from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def estudiante(request):
    return render (request, 'template_estudiante.html', context={})

def padre(request):
    return render (request, 'template_padre.html', context={})

def madre(request):
    return render (request, 'template_madre.html', context={})

def hermana(request):
    return render (request, 'template_hermana.html', context={})

def hermano(request):
    return render (request, 'template_hermano.html', context={})