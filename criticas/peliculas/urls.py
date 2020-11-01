from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('registro/', views.registro, name='registro'),
    path('endgame/', views.endgame, name='endgame'),
    path('dolittle/', views.dolittle, name='dolittle'),
    path('guerra/', views.guerra, name='guerra'),
    path('joker/', views.joker, name='joker'),
]

