from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
]
