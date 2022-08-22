from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def home(request):
    context = {
    }
    return render (request, 'home.html', context=context)

def estudiante(request):
    today = date.today
    context = {
        'name':'Vito',
        'last_name':'Masitti',
        'age':'31',
        'birth':'16/05/1991',
        'date':today
    }
    return render (request, 'estudiante.html', context=context)

def padre(request):
    today = date.today
    context = {
        'name':'Angel Gabriel',
        'last_name':'Masitti',
        'age':'62',
        'birth':'13/08/1960',
        'date':today
    }
    return render (request, 'padre.html', context=context)

def madre(request):
    today = date.today
    context = {
        'name':'Monica Rita',
        'last_name':'Gandini',
        'age':'56',
        'birth':'25/08/1966',
        'date':today
    }
    return render (request, 'madre.html', context=context)

def hermana(request):
    today = date.today
    context = {
        'name':'Bianca Sofia',
        'last_name':'Masitti',
        'age':'26',
        'birth':'07/04/996',
        'date':today
    }
    return render (request, 'hermana.html', context=context)

def hermano(request):
    today = date.today
    context = {
        'name':'Juan Pablo',
        'last_name':'Masitti',
        'age':'24',
        'birth':'08/10/1998',
        'date':today
    }
    return render (request, 'hermano.html', context=context)