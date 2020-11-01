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

    path('comentario/guerra', views.GuerraListView.as_view(), name='comentarioguerra'),
    path('comentario/guerra/<int:pk>', views.GuerraDetailView.as_view(), name='comentarioguerra-detail'),
    path('comentario/endgame', views.EndgameListView.as_view(), name='comentarioendgame'),
    path('comentario/endgame/<int:pk>', views.EndgameDetailView.as_view(), name='comentarioEndgame-detail'),
    path('comentario/joker', views.JokerListView.as_view(), name='comentariojoker'),
    path('comentario/joker/<int:pk>', views.JokerDetailView.as_view(), name='comentarioJoker-detail'),
    path('comentario/dolittle', views.DolittleListView.as_view(), name='comentariodolittle'),
    path('comentario/dolittle/<int:pk>', views.DolittleDetailView.as_view(), name='comentarioDolittle-detail'),
]

urlpatterns+=[
]