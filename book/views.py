from django.views.generic import ListView
from rest_framework import viewsets
from .models import Library,Author,Book
from .serializers import LibrarySerializer,AuthorSerializer,BookSerializer,LeadsSerializer
from .models import Book, Author, Library,Leads


class BookListView(ListView,viewsets.ModelViewSet):
    paginate_by = 100
    model = Book
    context_object_name = 'books'
    serializers_class = BookSerializer
    queryset = Book.objects.all()
    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs.order_by('title')
        return qs


class AuthorListView(ListView,viewsets.ModelViewSet):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class LibraryListView(ListView,viewsets.ModelViewSet):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

class LeadsListView(ListView,viewsets.ModelViewSet):
    model = Leads
    serializer_class = LeadsSerializer
    queryset = Library.objects.all()

#book_list_view = BookListView.as_view()
#author_list_view = AuthorListView.as_view()
#library_list_view = LibraryListView.as_view()