from datetime import datetime
from enum import auto

from django.db import models

# Create your models here.



class Empresas(models.Model):
    nombre_empresa = models.CharField(max_length=150, verbose_name='Nombre Empresas', unique=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'empresa'
        ordering = ['-id']

class Admin(models.Model):
    admin_empresas = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    usuario_admin =  models.CharField(max_length=150, verbose_name='Usuarios Admin', unique=True)
    contrasena =  models.CharField(max_length=150, verbose_name='Contraseñas')

    def __str__(self):
        return self.usuario_admin

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        db_table = 'admin'
        ordering = ['-id']

class Areas(models.Model):
    nombre_area = models.CharField(max_length=150, verbose_name='Nombre Areas')
    area_empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_area

    class Meta:
        verbose_name ='Area'
        verbose_name_plural ='Areas'
        db_table = 'areas'
        ordering = ['-id']


class Empleado(models.Model):
    type = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    empleado_area = models.ForeignKey(Areas, on_delete=models.PROTECT)
    nombre_empleado = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos_empleado = models.CharField(max_length=150, verbose_name='Apellidos')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    correo_electronico = models.CharField(max_length=150, verbose_name='Correo Electronico')
    telefono = models.IntegerField(verbose_name='Telefono')
    id_area = models.IntegerField(verbose_name='ID Area')
    id_empresa = models.IntegerField(verbose_name='ID Empresa')

    def __str__(self):
        return self.nombre_empleado

    class Meta:
        verbose_name ='Empleado'
        verbose_name_plural ='Empleados'
        db_table = 'empleado'
        ordering = ['-id']

class Usuarios(models.Model):
    usuario_empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    contrasena_empleado = models.CharField(max_length=150, verbose_name='Contraseñas Empleados')

    def __str__(self):
        return self.usuario_empleado

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        ordering = ['-id']

class Dispositivos (models.Model):
    nombre_dispositivo = models.CharField(max_length=150, verbose_name='Nombres Dispositivos')
    tipo_dispositivo = models.CharField(max_length=150, verbose_name=' Tipo Dispositivos')
    ubicacion_dispositivos = models.ForeignKey(Areas, on_delete=models.PROTECT)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    estado_dispositivo = models.CharField(max_length=150, verbose_name='Estado de Dispositivos ')
    diagnostico = models.CharField(max_length=350, verbose_name='Diagnostico de  Dispositivos')
    otras_especificaciones = models.CharField(max_length=350, verbose_name='Otras Especificaciones')

    def __str__(self):
        return self.nombre_dispositivo

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        db_table = 'dispositivos'
        ordering = ['id']

class Software (models.Model):
    numero_serie = models.ForeignKey(Dispositivos, on_delete=models.PROTECT)
    nombre_software = models.CharField(max_length=150, verbose_name=' Nombre de Software')
    descripcion_software =models.CharField(max_length=150, verbose_name=' Descripcion de Software')
    fecha_adquisición = models.DateField(auto_now=True)
    fecha_vencimiento = models.DateField(default=datetime.now, verbose_name='Fecha de vencimiento')

    def __str__(self):
        return self.nombre_software

    class Meta:
        verbose_name = 'Software'
        verbose_name_plural = 'Softwares'
        db_table = 'software'
        ordering = ['-id']