from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True, db_column='idUsuario')
    nombreUsuario = models.TextField(max_length=50, db_column='nombreUsuario')
    apellidoPaterno = models.TextField(max_length=50, db_column='apellidoPaterno')
    apellidoMaterno = models.TextField(max_length=50, db_column='apellidoMaterno')
    password = models.TextField(max_length=128)  # El campo de contraseña se maneja automáticamente encriptado
    correoElectronico = models.EmailField(unique=True, db_column='correoElectronico')
    numeroTelefonico = models.IntegerField(db_column='numeroTelefonico')

    def __str__(self):
        return self.username  # Puedes elegir qué campo usar como representación en cadena (string) del usuario
