# Create your models here.

from django.db import models
import uuid
class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)

    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class cultivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.IntegerField(verbose_name='codigo', default=1)
    latitud = models.IntegerField(verbose_name='latitud', default=1)
    longitud = models.IntegerField(verbose_name='longitud', default=1)
    area = models.IntegerField(verbose_name='area', default=1)
    producto = models.CharField(verbose_name='producto', max_length=20)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
