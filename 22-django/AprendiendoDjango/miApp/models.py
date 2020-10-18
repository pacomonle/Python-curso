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
    title = models.CharField(max_length = 150, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default = 'null', verbose_name='Miniatura', upload_to='articles') # indicar donde guardar los archivos
    public = models.BooleanField(verbose_name='¿Publicado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        """
        organizacion interna del model
        """
        verbose_name = 'Articulo' # renombrar el modelo
        verbose_name_plural = 'Articulos'
        ordering = ['-id'] # criterio de ordenacion ['public']
        pass
    # metodo para imprimir objetos en el admin panel
    # ver documentacion magic methods django
    def __str__(self):
        if self.public:
            publico = 'publicado'
            pass
        else:
            publico = 'privado'
            pass
        return f'{self.title} - ({publico})'
    
    pass
class Category(models.Model):
    """
    modelo categoria
    """
    name = models.CharField(max_length = 150, verbose_name='Nombre')
    description = models.CharField(max_length = 275, verbose_name='Descripcion')
    created_at = models.DateField() 
    class Meta:
        """
        organizacion interna del model
        """
        verbose_name = 'Categoria' # renombrar el modelo
        verbose_name_plural = 'Categorias'
        
        pass
    pass

"""
class Meta de los modelos :
- para configurar el funcionamiento interno de los modelos
- meta class django ver documentacion
"""