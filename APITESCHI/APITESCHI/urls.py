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
from api.views import login, home, shop,my_account,about_us,account_details,addresses,cart
from api.views import index_3,order_list,product_details
from api.views import wishlist
from api.views import shop_list_right_sidebar


urlpatterns = [
    #lo comentamos para que no se inicie con la ventana de django
    #path('admin/', admin.site.urls),

    #se crea, el path de vista con el home creado nombrandolo login
   
   path('login/',login.as_view(),name='login'),
   path('',home.as_view(),name='home'),
   path('shop/',shop.as_view(),name='shop'),   
   path('my_account/',my_account.as_view(),name='my_account'),
   path('about_us/',about_us.as_view(),name='about_us'),
   path('account_details/',account_details.as_view(),name='account_details'),
   path('addresses/',addresses.as_view(),name='addresses'),
   path('cart/',cart.as_view(),name='cart'),
   path('index_3/',index_3.as_view(),name='index_3'),
   path('order_list/',order_list.as_view(),name='order_list'),
   path('product_details/',product_details.as_view(),name='product_details'),
   path('wishlist/',wishlist.as_view(),name='wishlist'),
   path('shop_list_right_sidebar/',shop_list_right_sidebar.as_view(),name='shop_list_right_sidebar'),
    #path('admin/',admin.site.urls)
]

