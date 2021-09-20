from django.views.generic import ListView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Library,Author,Book
from .serializers import LibrarySerializer,AuthorSerializer,BookSerializer,LeadsSerializer
from .models import Book, Author, Library,Leads


class BookListView(viewsets.ModelViewSet):
    paginate_by = 100
    model = Book
    context_object_name = 'books'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['id']
    search_fields = ['title']

class AuthorListView(viewsets.ModelViewSet):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class LibraryListView(viewsets.ModelViewSet):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
   

class LeadsListView(viewsets.ModelViewSet):
    paginate_by = 100
    model = Leads
    context_object_name = 'leads'
    serializer_class = LeadsSerializer
    queryset = Leads.objects.all()

#book_list_view = BookListView.as_view()
#author_list_view = AuthorListView.as_view()
#library_list_view = LibraryListView.as_view()