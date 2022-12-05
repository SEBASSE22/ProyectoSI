from django.shortcuts import render
from core.Inventario.models import Dispositivos

def tecnicos(request):
    data = {
        'title': ' Mantenimiento',
        'dispositivos': Dispositivos.objects.all()        
    }
    return render(request, 'tecnicos/inicio_tecnico.html', data)