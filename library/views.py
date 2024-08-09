from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Category, Book
from .filters import BookFilter

# Create your views here.
class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'library/form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')


class BookListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset.form
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset)
        return self.filterset.qs


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    template_name = 'library/form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    success_url = 'book-list'
