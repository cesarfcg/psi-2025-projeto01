from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elenco/', views.elenco, name='elenco'),
    path('sobre/', views.sobre, name='sobre'),
    path('jogador/<int:id_jogador>', views.jogador, name='jogador'),
    path('noticia/<int:id_noticia>', views.noticia, name='noticia'),
    
]
