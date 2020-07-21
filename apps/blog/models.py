from django.db import models
from  ckeditor.fields import RichTextField

# Create your models here.
class Categoria (models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',max_length=50, blank = False, null = False)
    estado = models.BooleanField('Categoria Activada o Inactivada', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self): 
        return self.nombre
    
class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del autor', max_length=100, blank = False, null = False)
    apellidos = models.CharField('Apellidos del autor', max_length=100, blank = False,  null = False )
    facebook =  models.URLField('Facebook', null = True, blank = True)
    twitter =  models.URLField('twitter', null = True, blank = True)
    instagram =  models.URLField('instagram', null = True, blank = True)
    web =  models.URLField('web', null = True, blank = True)
    correo = models.EmailField('Correo electronico', null = True, blank = True)
    estado = models.BooleanField('Autor activo o inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)
    
     
    class Meta:        
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return "{0},{1}".format(self.nombre,self.apellidos)
    
class Post(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=100, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 250, blank = False, null = False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField(max_length = 255, blank = False, null = False)
    autor_id = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicada o No publicada', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
        
    def __str__(self):
        return self.titulo