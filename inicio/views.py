from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1> Soy la pantalla de inicio </h1>')
