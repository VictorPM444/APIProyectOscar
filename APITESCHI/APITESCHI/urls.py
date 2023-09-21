"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#se importa la vista de la API desde el Home que hicimos antes
from api.views import login, home, shop, formulario,gallery,my_account


urlpatterns = [
    #lo comentamos para que no se inicie con la ventana de django
    #path('admin/', admin.site.urls),

    #se crea, el path de vista con el home creado nombrandolo login
   
   path('login/',login.as_view(),name='login'),
   path('',home.as_view(),name='home'),
   path('shop/',shop.as_view(),name='shop'),   
   path('registro/',formulario.as_view(),name='registro'),   
   path('gallery/',gallery.as_view(),name='gallery'),
   path('my_account/',my_account.as_view(),name='my_account'),

    #path('admin/',admin.site.urls)
]

