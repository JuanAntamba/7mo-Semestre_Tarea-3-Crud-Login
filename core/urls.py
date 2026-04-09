"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from pedidos import views
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('cuentas/', include('django.contrib.auth.urls')), 
    
    
    path('panel/', views.panel_estudiante, name='panel'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')), 
    path('panel/', views.panel_estudiante, name='panel'),
    
    # NUEVA RUTA: La URL necesita el ID del pedido para saber cuál borrar
    path('cancelar/<int:pedido_id>/', views.cancelar_pedido, name='cancelar_pedido'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')), 
    path('panel/', views.panel_estudiante, name='panel'),
    path('cancelar/<int:pedido_id>/', views.cancelar_pedido, name='cancelar_pedido'),
    
    # NUEVA RUTA: Para editar el pedido
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    
    path('', RedirectView.as_view(url='/panel/')), 
]