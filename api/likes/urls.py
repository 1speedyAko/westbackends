from django.urls import path
from . import views

#class based views
urlpatterns = [
     
     path('login/', views.UserLoginView.as_view(), name='login'),
     path('logout/', views.UserLogoutView.as_view(), name='logout'),
     path('register/', views.UserRegister.as_view(), name='register'),
     path('user/', views.UserView.as_view(), name='user'),

]