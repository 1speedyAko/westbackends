from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from . views import home


urlpatterns = [
   
    path('', home),
    path('users/', include('api.users.urls')),
    path('products/', include('api.products.urls')),
    path('orders/', include('api.orders.urls')),
  

]
