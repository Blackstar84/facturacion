from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) # Fecha de Creación con auto_now_add sólo se agregará este campo cuando se crea un registro
    fm = models.DateTimeField(auto_now=True) # Fecha de Modificación con auto_now se modificará esta fecha cada vez que se modifique algún campo del registro
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario que crea el registro, este será el id que se asociará al Usuario
    um = models.IntegerField(blank=True, null=True) # Usuario modifica este campo sera integer que guardará el id de la tabla User
    
    
    class Meta:
        abstract = True # Al agregar abstract = True este modelo no va a ser tenido en cuenta a la hora de realizar las migraciones, pero si se va a poder heredar del mismo


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) # Fecha de Creación con auto_now_add sólo se agregará este campo cuando se crea un registro
    fm = models.DateTimeField(auto_now=True) # Fecha de Modificación con auto_now se modificará esta fecha cada vez que se modifique algún campo del registro
    #uc = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario que crea el registro, este será el id que se asociará al Usuario
    #um = models.IntegerField(blank=True, null=True) # Usuario modifica este campo sera integer que guardará el id de la tabla User
    uc = UserForeignKey(auto_user_add=True, related_name='+') # con el más no va a asignar un nombre a la búsqueda que vamos a hacer
    um = UserForeignKey(auto_user=True, related_name='+')
    
    class Meta:
        abstract = True # Al agregar abstract = True este modelo no va a ser tenido en cuenta a la hora de realizar las migraciones, pero si se va a poder heredar del mismo        