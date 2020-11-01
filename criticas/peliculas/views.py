from django.shortcuts import render
from .models import ComentarioEndgame,ComentarioDolittle,ComentarioGuerra,ComentarioJoker
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    return render(
        request,
        'index.html',
    )

def galeria(request):

    return render(
        request,
        'galeria.html',
    )

def registro(request):

    return render(
        request,
        'registro.html',
    )

def endgame(request):
    comentario=ComentarioEndgame.objects.all()
    return render(
        request,
        'endgame.html',
        context={'comentario':comentario},
    )

def dolittle(request):
    comentario=ComentarioDolittle.objects.all()
    return render(
        request,
        'dolittle.html',
        context={'comentario':comentario},
    )

def guerra(request):
    comentario=ComentarioGuerra.objects.all()
    return render(
        request,
        'guerra.html',
        context={'comentario': comentario},
    )

def joker(request):
    comentario=ComentarioJoker.objects.all()
    return render(
        request,
        'joker.html',
        context={'comentario':comentario},
    )


