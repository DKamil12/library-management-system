import django_filters
from .models import Book, Category
from django import forms

class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Book'}),
        label=''
    )
    author__name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Author'}),
        label=''
    )
    published_at = django_filters.DateFilter(
        field_name='published_at', 
        lookup_expr='exact', 
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label=''
        )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'placeholder': 'Category'}),
        label=''
        )
    
    class Meta:
        model = Book
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['category'].widget.choices = [('', 'Category')] + list(self.form.fields['category'].widget.choices)