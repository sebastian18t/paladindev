from django.urls import path
from .views import Home, Generales, Programacion, Tecnologia, Videojuegos, Tutoriales, DetailPost

urlpatterns = [
    path('', Home, name = 'pg_Home'), 
    path('generales/', Generales, name='pg_Gnrls'),
    path('programacion/', Programacion, name='pg_Progm'),
    path('tecnologia/', Tecnologia, name='pg_Tecno'),
    path('videojuegos/', Videojuegos, name='pg_Vjuegos'),
    path('tutoriales/', Tutoriales, name='pg_Tuto'),
    path('<slug:slug>/', DetailPost, name = 'detail_Post')
]
