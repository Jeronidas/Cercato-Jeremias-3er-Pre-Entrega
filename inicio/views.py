from django.http import HttpResponse
from django.template import Template, context, loader
from datetime import datetime
from django.shortcuts import render

def inicio(request):
    # return HttpResponse('<h1> Soy la pantalla de inicio </h1>')
    return render(request, 'index.html')