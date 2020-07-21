from django.contrib import admin
from .models import Categoria, Autor, Post

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor

class PostResources(resources.ModelResource):
    class Meta:
        model = Post
        
class CategoriaAdmin(ImportExportActionModelAdmin, admin.ModelAdmin): 
    search_fields = ['nombre']
    list_display = ('nombre', 'estado','fecha_creacion')
    resources_class = CategoriaResources
    
class AutorAdmin (ImportExportActionModelAdmin,admin.ModelAdmin): 
    search_fields =['nombre','apellidos', 'correo']
    list_display = ('nombre', 'apellidos','correo', 'estado')
    resource_class = AutorResources 

class PostAdmin (ImportExportActionModelAdmin,admin.ModelAdmin): 
    resource_class = PostResources 
    
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin) 
