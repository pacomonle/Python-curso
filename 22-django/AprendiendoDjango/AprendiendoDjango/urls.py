"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importar app con las views
from miApp import views
# para cargar imagenes importar los settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas
    path('', views.index, name='index'),
    path('inicio/', views.index, name= 'inicio'),
    path('hola-django/', views.hola_mundo, name = 'hola_django'),
    path('hola-django/<int:redirigir>', views.hola_mundo, name = 'hola_django'),
    path('page/', views.pagina, name='page'),
    path('page/<str:nombre>', views.pagina, name='page'),
    path('page/<str:nombre>/<str:secciones>', views.pagina, name='page'),
    path('contact/', views.contacto, name='contacto'),
 
    path('articulo/', views.articulo, name='articulo'),
    path('editar-articulo/<str:id>', views.editar_articulo, name='editar_articulo'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name='nuevo_articulo'),
    path('articulos/', views.articulos, name='articulos'),
    path('borrar-articulo/<str:id>', views.borrar_articulo, name='borrar_articulo'),
    path('create-article/', views.create_article, name='crear_articulo'),
    path('save-article/', views.save_article, name='guardar_articulo'),

    path('create-full-article/', views.create_full_article, name='create_full_articulo'),
]

# Configuracion para cargar las imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    pass
"""
# Configuracion titulo del admin panel
title = 'Master Python y Django'
admin.site.site_header= title
admin.site.site_title= title
admin.site.index_title= 'PANEL de GESTION'
"""