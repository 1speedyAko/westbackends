from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('api/category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]
