from django.test import TestCase

from config.wsgi import *

# Create your tests here.

from core.Inventario.models import Empresas

#Listar

#select * from Tabla

query = Empresas.objects.all()
print(query)

#Insercion

#empresa = Empresas()
#empresa.nombre_empresa= 'nombre'
#empresa.save()

#Edicion
# empresa=Empresas.object.get(id=1 o pk=1)
#
#Eliminación
#empresa =Empresas.objects.get(pk=1)
#empresa.delete()


#Filtros
#Empresas.object.filter()