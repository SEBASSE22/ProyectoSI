from django.shortcuts import render


def admins(request):
    data = {
        'title': 'Administrador',
        
    }
    return render(request, 'admin/inicio_admin.html', data)