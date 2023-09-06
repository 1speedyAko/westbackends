from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from . views import home


urlpatterns = [
   
    path('', home),
    path('category/', include('api.category.urls')),
  

]
