from django.urls import path
from . import views

urlpatterns = [
    path('pag_cadastro/', views.pag_cadastro, name='pag_cadastro'),
    path('pag_logar/', views.pag_logar, name='pag_logar'),
    path('cadastramento/', views.cadastramento, name='cadastramento'),
    path('logar/', views.logar, name='logar'),
    path('deslogar/', views.deslogar,name='deslogar'),
    ]