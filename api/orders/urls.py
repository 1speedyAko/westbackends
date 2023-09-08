from django.urls import path,include
from .views import OrderListCreateView


from . import views

urlpatterns = [
	
	path('orders/',OrderListCreateView.as_view(),name = 'Order-list-create-view'),
	path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
	path('order-items/', views.OrderItemCreateView.as_view(), name='order-item-create'),
]