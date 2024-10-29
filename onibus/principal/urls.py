from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_principal, name='site_principal'),
    path('vizualizacao/', views.vizualizacao, name='vizualizacao'),
    path('checar/<int:id>', views.checar, name='checar'),
    path('comprar/<int:id>',views.comprar, name='comprar'),
    path('comprar_pas/',views.comprar_pas, name='comprar_pas'),
    path('agenda/',views.agenda, name='agenda'),

    
    ]