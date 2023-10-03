from django.urls import path,include
from api.cart.views import CartView, RemoveFromCartView, AddToCartView
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')
router.register(r'remove-from-cart', RemoveFromCartView, basename='remove-from-cart')
router.register(r'add-to-cart', AddToCartView, basename='add-to-cart')

urlpatterns = [
    path('cart', include(router.urls)),
    path('remove-from-cart/',include (router.urls)),
    path('add-to-cart/', include(router.urls)),
]
