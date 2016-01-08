from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=66)
	serie = models.CharField(max_length=66)
	marca= models.CharField(max_length=66)


class Publicacion(models.Model):
	nombre = models.CharField(max_length=66)
	precio_producto = models.IntegerField()
	unidades = models.IntegerField()
	descripcion = models.TextField(max_length=200)
	estado = models.CharField(max_length=66)
	def __unicode__(self):
		return self.nombre
		
class Transaccion(models.Model):
	fecha = models.DateField()
	comentario = models.TextField(max_length=200)

class Categoria(models.Model):
	nombre = models.CharField(max_length=66)			

class Beneficio(models.Model):	
	precio = models.IntegerField()
	tipo_beneficio= models.CharField(max_length=66)