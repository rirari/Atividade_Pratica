from django.shortcuts import render
from .models import Locacao, Filme

# Create your views here.
def index(request):
    return render(request,'locadora/index.html')

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locadora/locacao.html', {'locacoes': locacoes})

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'locadora/filmes.html', {'filmes': filmes})