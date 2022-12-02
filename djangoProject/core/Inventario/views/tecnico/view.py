from django.shortcuts import render


def tecnicos(request):
    data = {
        'title': 'Mantenimiento',
        
    }
    return render(request, 'empleados/inicio_empleado.html', data)