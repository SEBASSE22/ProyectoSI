from django.contrib import admin
from django.urls import path, include
from core.Inventario.views.Empresas.view import empleados
from core.Inventario.views.login.view import login
from core.Inventario.views.tecnico.view import tecnicos


urlpatterns = [
    path('', login, name='login'),
    path('empleado/inicio', empleados, name='empleado_inicio'),
    path('tecnico/inicio', tecnicos, name='tecnico_inicio'),
]