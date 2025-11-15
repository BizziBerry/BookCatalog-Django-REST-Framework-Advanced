from django.urls import path
from .views import (
    BookListCreateAPIView, 
    BookDetailAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryDetailView
)

urlpatterns = [
    # Маршруты для книг
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    
    # Маршруты для категорий
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category-detail-books'),
]