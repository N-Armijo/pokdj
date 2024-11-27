"""
URL configuration for gestion_pokemones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from pokemones.views import crear_pokemon,editar_pokemon,eliminar_pokemon,listar_pokemon, registro_usuario, pagina_principal
from tipos.views import crear_tipo,editar_tipo,eliminar_tipo,listar_tipo
from evoluciones.views import crear_evolucion,eliminar_evolucion,listar_evolucion,editar_evolucion
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pagina_principal, name='pagina_principal'),

    path('registro/',registro_usuario, name='registro_usuario'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Pokémon
    path('listar_pokemon/', listar_pokemon, name='listar_pokemon'),
    path('crear_pokemon/', crear_pokemon, name='crear_pokemon'),
    path('editar_pokemon/<int:pokemon_id>/', editar_pokemon, name='editar_pokemon'),
    path('eliminar_pokemon/<int:pokemon_id>/', eliminar_pokemon, name='eliminar_pokemon'),

    # Tipos
    path('listar_tipo/', listar_tipo, name='listar_tipo'),
    path('crear_tipo/', crear_tipo, name='crear_tipo'),
    path('editar_tipo/<int:tipo_id>/', editar_tipo, name='editar_tipo'),
    path('eliminar_tipo/<int:tipo_id>/', eliminar_tipo, name='eliminar_tipo'),

    # Evoluciones
    path('listar_evolucion/', listar_evolucion, name='listar_evolucion'),
    path('crear_evolucion/', crear_evolucion, name='crear_evolucion'),
    path('eliminar_evolucion/<int:evolucion_id>/', eliminar_evolucion, name='eliminar_evolucion'),
    path('editar_evolucion/<int:evolucion_id>/', editar_evolucion, name='editar_evolucion'),
]
