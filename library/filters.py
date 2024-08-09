import django_filters
from .models import Book
from django import forms

class BookFilter(django_filters.FilterSet):
    author__name = django_filters.CharFilter(lookup_expr='icontains')
    published_at = django_filters.DateFilter(field_name='published_at', lookup_expr='exact', widget=forms.DateInput(attrs={'type': 'date'}), label='Publish year')
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = {
            'name': ['icontains'],
        }