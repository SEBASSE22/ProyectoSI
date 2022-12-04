from django.shortcuts import render


def tecnicos(request):
    data = {
        'title': 'Mantenimiento',
        
    }
    return render(request, 'tecnicos/inicio_tecnico.html', data)