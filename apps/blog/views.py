from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q #ES EL "O" LOGICO 
from django.core.paginator import Paginator

# Create your views 
def Home(request):
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(estado = True)
    
    if queryset: 
        posts = Post.objects.filter(
                Q(titulo__icontains = queryset) |
                Q(descripcion__icontains = queryset),
                estado = True
            ).distinct() #solo me trae el de uno de los dos
    
    paginator =   Paginator(posts, 2) #listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    page = request.GET.get('page') # obtiene le número de la pagina actual para saber cual sigue
    posts = paginator.get_page(page) #se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
    
    return render(request, 'index.html', {'posts': posts })

def Generales(request):
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(
        estado = True,
        categoria_id = Categoria.objects.get(nombre__iexact = 'Generales')
    )
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria_id = Categoria.objects.get(nombre__iexact = 'Generales')
        ).distinct()  # solo me trae el de uno de los dos
    
    # listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    paginator = Paginator(posts, 2)
    # obtiene le número de la pagina actual para saber cual sigue
    page = request.GET.get('page')
    # se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
    posts = paginator.get_page(page)
    
    return render(request, 'generales.html', {'posts': posts})

def Programacion(request): 
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(
        estado = True,
        categoria_id = Categoria.objects.get(nombre__iexact ='Programacion')
    )
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria_id = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()  # solo me trae el de uno de los dos
    
    # listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    paginator = Paginator(posts, 2)
    # obtiene le número de la pagina actual para saber cual sigue
    page = request.GET.get('page')
    # se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
    posts = paginator.get_page(page)
    
    return render(request, 'programacion.html', {'posts': posts})

def Tecnologia(request): 
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(
        estado = True,
        categoria_id = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria_id = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()  # solo me trae el de uno de los dos
    
    paginator =   Paginator(posts, 2) #listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    page = request.GET.get('page') # obtiene le número de la pagina actual para saber cual sigue
    posts = paginator.get_page(page) #se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
        
    return render(request, 'tecnologia.html', {'posts': posts})

def Videojuegos(request): 
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(
        estado = True,
        categoria_id = Categoria.objects.get(nombre__iexact ='Videojuegos')
    )
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria_id = Categoria.objects.get(nombre__iexact = 'Videojuegos')
        ).distinct()  # solo me trae el de uno de los dos
    
    # listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    paginator = Paginator(posts, 2)
    # obtiene le número de la pagina actual para saber cual sigue
    page = request.GET.get('page')
    # se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
    posts = paginator.get_page(page)
    
    return render(request, 'videojuegos.html', {'posts': posts})

def Tutoriales(request): 
    
    queryset = request.GET.get('buscar') 
    posts = Post.objects.filter(
        estado = True,
        categoria_id = Categoria.objects.get(nombre__iexact ='Tutoriales')
    )
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria_id = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()  # solo me trae el de uno de los dos
    
    paginator =   Paginator(posts, 2) #listado de elementos a mostrar, y la cantidad de elementos a mostrar x pg
    page = request.GET.get('page') # obtiene le número de la pagina actual para saber cual sigue
    posts = paginator.get_page(page) #se sobre escribe posts, porque con esto se controla aquellos posts para la pg siguiente
            
    return render(request, 'tutoriales.html', {'posts': posts})

def DetailPost(request, slug): 
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detail_post':post})
    
