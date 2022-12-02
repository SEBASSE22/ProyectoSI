from django.shortcuts import render
from core.Inventario.models import Empresas

def empleados(request):
    data = {
        'title': 'Listado de Empresas',
        'empresas': Empresas.objects.all()
    }
    return render(request, 'empleados/inicio_empleado.html', data)


