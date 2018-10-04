from django.http import HttpResponse

from django.shortcuts import render
from productos.models import Producto

def __main__(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', { 'productos' : productos})
