from django.urls import path
from . import views

app_name='familires_app'

urlpatterns = [
    path('familiares/', views.traer_registros, name='familiares'),
]