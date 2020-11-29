from django.shortcuts import render
from django.http import HttpResponse
from .form import Escolasform
# Create your views here.
def index(request):
    #return HttpResponse("<h1> Aqui é o index<h1>")
    return render(request, 'Escolas/index.html')


def Escolas(request):
    return  HttpResponse("<h1> Aqui é a area da Escola<h1>")

    def criar_Escola (request):
    	form = Escolasform(request.POST)
    	if form.is_valid():
    		esc = form.save()
    		esc.save()
    		form = Escolasform()
    	return render(request, 'Escola/criar_Escola.html', {'form':form})