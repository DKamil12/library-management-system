from django.urls import path
from .views import CategoryListView, CategoryCreateView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('books/new', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]
