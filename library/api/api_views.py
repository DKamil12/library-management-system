from rest_framework import generics
from rest_framework import viewsets, filters
from .serializers import BookListSerializer, CategorySerializer, BookCreateSerializer, AuthorSerializer
from library.models import Book, Category, Author
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


# ModelViewSets

class AuthorAPIViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['name']
    

class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['name']


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'category']
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListSerializer
        else:
            return BookCreateSerializer