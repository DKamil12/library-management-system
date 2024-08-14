from django.urls import path, include
from .views import CategoryListView, CategoryCreateView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .api.api_views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'category', CategoryAPIViewSet)
router.register(r'book', BookAPIViewSet)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/new/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<str:category>/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # API
    path('api/v1/book/', BookListCreateAPIView.as_view()),
    path('api/v1/book/<int:pk>/', BookDetailUpdateDeleteAPIView.as_view()),
    path('api/v1/category/', CategoryListCreateAPIView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryDetailUpdateDeleteAPIView.as_view()),
    
    # ViewSets
    path('api/v2/', include(router.urls)),
]
