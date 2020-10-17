from django.db import models

"""
- el modelo es una tabla de la base de datos
- aunque tambien puede ser un registro concretod e la tabla
"""
# Create your models here.

class Article(models.Model):
    """
    modelo articulo
    """
    title = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(default = 'null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass
class Category(models.Model):
    """
    modelo categoria
    """
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 275)
    created_at = models.DateField() 
    pass
