from django.db import models

# Create your models here.
#Aqui se crea el modelo de la BD (esqueleto)

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True,db_column='idGenero')
    nombreMarca = models.TextField(db_column='nombreMarca')
    class Meta:
        db_table='Marcas'

