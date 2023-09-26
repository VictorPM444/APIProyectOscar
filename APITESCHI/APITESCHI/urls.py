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
from api.views import login, home, shop,my_account,shop_grid_left_sidebar,about_us,account_details,addressws,cart
from api.views import coming_soon,compare,contact,downloads,faq,heading,index_3,index,modals,order_list,product_details,register
from api.views import wishlist,shop_grid_no_sidebar,shop_grid_right_sidebar,shop_grid_top_sidebar,shop_list_left_sidebar,shop_list_no_sidebar
from api.views import shop_list_right_sidebar,shop_list_top_sidebar


urlpatterns = [
    #lo comentamos para que no se inicie con la ventana de django
    #path('admin/', admin.site.urls),

    #se crea, el path de vista con el home creado nombrandolo login
   
   path('login/',login.as_view(),name='login'),
   path('',home.as_view(),name='home'),
   path('shop/',shop.as_view(),name='shop'),   
   path('my_account/',my_account.as_view(),name='my_account'),
   path('shop_grid_left_sidebar/',shop_grid_left_sidebar.as_view(),name='shop_grid_left_sidebar'),
   path('about_us/',about_us.as_view(),name='about_us'),
   path('account_details/',account_details.as_view(),name='account_details'),
   path('addressws/',addressws.as_view(),name='addressws'),
   path('cart/',cart.as_view(),name='cart'),
   path('coming_soon/',coming_soon.as_view(),name='coming_soon'),
   path('compare/',compare.as_view(),name='compare'),
   path('contact/',contact.as_view(),name='contact'),
   path('downloads/',downloads.as_view(),name='downloads'),
   path('faq/',faq.as_view(),name='faq'),
   path('heading/',heading.as_view(),name='heading'),
   path('index_3/',index_3.as_view(),name='index_3'),
   path('index/',index.as_view(),name='index'),
   path('modals/',modals.as_view(),name='modals'),
   path('order_list/',order_list.as_view(),name='order_list'),
   path('product_details/',product_details.as_view(),name='product_details'),
   path('register/',register.as_view(),name='register'),
   path('wishlist/',wishlist.as_view(),name='wishlist'),
   path('shop_grid_no_sidebar/',shop_grid_no_sidebar.as_view(),name='shop_grid_no_sidebar'),
   path('shop_grid_right_sidebar/',shop_grid_right_sidebar.as_view(),name='shop_grid_right_sidebar'),
   path('shop_grid_top_sidebar/',shop_grid_top_sidebar.as_view(),name='shop_grid_top_sidebar'),
   path('shop_list_left_sidebar/',shop_list_left_sidebar.as_view(),name='shop_list_left_sidebar'),
   path('shop_list_no_sidebar/',shop_list_no_sidebar.as_view(),name='shop_list_no_sidebar'),
   path('shop_list_right_sidebar/',shop_list_right_sidebar.as_view(),name='shop_list_right_sidebar'),
   path('shop_list_top_sidebar/',shop_list_top_sidebar.as_view(),name='shop_list_top_sidebar'),

    #path('admin/',admin.site.urls)
]

