from rest_framework import serializers
from library.models import Book, Category, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class AuthorForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class CategoryForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    category = CategoryForBookSerializer(read_only=True)
    author = AuthorForBookSerializer(read_only=True)

    class Meta:
        model = Book
        exclude = []