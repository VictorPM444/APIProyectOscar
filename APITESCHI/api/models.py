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

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,db_column='idCategoria')
    nombreCategoria = models.TextField(max_length=50,db_column='nombreCategoria')
    descripcion = models.TextField(max_length=150,db_column='descripcion')
    class Meta:
        db_table='Categorias'







