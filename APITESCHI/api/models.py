from django.db import models

# Create your models here.
#Aqui se crea el modelo de la BD (esqueleto)

#########################  ENTIDADES  #####################

#metodo para la creacion de la entidad marca
class Marca(models.Model):
    #creadion de ID autoincrementable y como llave primaria
    idMarca = models.AutoField(primary_key=True,db_column='idGenero')
    #creacion de atributos de entidad
    nombreMarca = models.TextField(max_length=20,db_column='nombreMarca')
    descripcion = models.TextField(max_length=150,db_column='descripcion')
    #metodo de nombramiento de la entidad
    class Meta:
        db_table='Marcas'

class Talla(models.Model):
    idTalla = models.AutoField(primary_key=True,db_column='idTalla')
    nombreColor = models.TextField(max_length=20,db_column='nombreColor')
    class Meta:
        db_table='Tallas'





