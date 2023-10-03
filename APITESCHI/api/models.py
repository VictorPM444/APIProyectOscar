from .models import models

# Create your models here.
#Aqui se crea el modelo de la BD (esqueleto)

#########################  ENTIDADES  #####################

#metodo para la creacion de la entidad marca
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

class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True, db_column='idMaterial')
    nombreMaterial = models.TextField(max_length=30,db_column='nombreMaterial')
    class Meta:
        db_table='Materiales'

class Temporada(models.Model):
    idTemporada = models.AutoField(primary_key=True,db_column='idTemporada')
    nombreTemporada = models.TextField(max_length=30,db_column='nombreTemporada')
    class Meta:
        db_table='Temporadas'

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,db_column='idGenero')
    nombreGenero = models.TextField(max_length=20,db_column='nombreGenero')
    class Meta:
        db_table='Generos'

class Talla(models.Model):
    idTalla = models.AutoField(primary_key=True,db_column='idTalla')
    nombreTalla = models.FloatField(db_column='nombreTalla')
    class Meta:
        db_table='Tallas'

class Color(models.Model):
    idColor = models.AutoField(primary_key=True,db_column='idColor')
    nombreColor = models.TextField(max_length=30, db_column='nombreColor')
    class Meta:
        db_table='Colores'

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True,db_column='idUsuario')
    nombreUsuario = models.TextField(max_length=50,db_column='nombreUsuario')
    apellidoPaterno = models.TextField(max_length=50,db_column='apellidoPaterno')
    apellidoMaterno = models.TextField(max_length=50,db_column='apellidoMaterno')
    password = models.TextField(max_length=25,db_column='password')
    correoElectronico = models.EmailField(unique=True,db_column='correoElectronico')
    numeroTelefonico = models.IntegerField(db_column='numeroTelefonico')
    class Metas:
        db_table='Usuarios'

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True,db_column='idPedido')
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='fk_usuario')
    fechaPedido = models.DateField(db_column='fechaPedido')
    direccionEnvio = models.TextField(max_length=200,db_column='direccionEnvio')
    estadoPedido = models.TextField(max_length=20,db_column='estadoPedido')
    totalPedido = models.FloatField(db_column='totalPedido')
    metodoPago = models.TextField(max_length=20,db_column='metodoPago')
    class Meta:
        db_table='Pedidos'

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,db_column='idProducto')
    nombreProducto = models.TextField(max_length=50,db_column='nombreProducto')
    descripcionProducto = models.TextField(max_length=100,db_column='descripcionProducto')
    precioProducto =models.FloatField(db_column='precioProducto')
    imagenProducto = models.ImageField(db_column='imagenProducto')
    disponibilidadStock = models.IntegerField(db_column='disponibilidadStock')
    fk_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,db_column='fk_categoria')
    fk_material = models.ForeignKey(Material,on_delete=models.CASCADE,db_column='fk_material')
    fk_marca = models.ForeignKey(Marca,on_delete=models.CASCADE,db_column='fk_marca')
    fk_talla = models.ForeignKey(Talla,on_delete=models.CASCADE,db_column='fk_talla')
    fk_color = models.ForeignKey(Color,on_delete=models.CASCADE,db_column='fk_color')
    fk_temporada = models.ForeignKey(Temporada,on_delete=models.CASCADE,db_column='fk_temporada')
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='Producto'

class CarroCompras(models.Model):
    idCarroCompras = models.AutoField(primary_key=True,db_column='idCarroCompras')
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='fk_usuario')
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,db_column='fk_producto')
    numeroProducto = models.IntegerField(db_column='numeroProducto')
    class Meta:
        db_table='CarroCompras'

class Resena(models.Model):
    idResena = models.AutoField(primary_key=True, db_column='idResena')
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,db_column='fk_producto')
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='fk_usuario')
    puntuacion = models.IntegerField(db_column='puntuacion')
    comentario = models.TextField(max_length=200,db_column='comentario')
    class Meta:
        db_table='Resenas'

#Tablas de muchos a muchos
class Producto_has_Categoria(models.Model):
    id_Producto_has_Categoria = models.AutoField(primary_key=True,db_column='id_Producto_has_Categoria')
    fk_id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='fk_id_Producto')
    fk_id_Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,db_column='fk_id_Categoria')
    class Meta:
        db_table='Producto_has_Categoria'

class Producto_has_Color(models.Model):
    id_Producto_has_Color = models.AutoField(primary_key=True,db_column='id_Producto_has_Color')
    fk_id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='fk_id_Producto')
    fk_id_Color = models.ForeignKey(Color, on_delete=models.CASCADE,db_column='fk_id_Color')
    class Meta:
        db_table='Producto_has_Color'

class Producto_has_Talla(models.Model):
    id_Producto_has_Talla = models.AutoField(primary_key=True,db_column='id_Producto_has_Talla')
    fk_id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='fk_id_Producto')
    fk_id_Talla = models.ForeignKey(Talla, on_delete=models.CASCADE,db_column='fk_id_Talla')
    class Meta:
        db_table='Producto_has_Talla'

class Producto_has_Material(models.Model):
    id_Producto_has_Material = models.AutoField(primary_key=True,db_column='id_Producto_has_Material')
    fk_id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE,db_column='fk_id_Producto')
    fk_id_Material = models.ForeignKey(Material, on_delete=models.CASCADE,db_column='fk_id_Material')
    class Meta:
        db_table='Producto_has_Material'

class Usuario_Pedido(models.Model):
    id_Usuario_has_Pedido = models.AutoField(primary_key=True,db_column='id_Usuario_has_Pedido')
    fk_id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,db_column='fk_id_Usuario')
    fk_id_Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,db_column='fk_id_Pedido')
    class Meta:
        db_table='Usuario_Pedido'















