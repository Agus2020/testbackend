from django.views.generic import ListView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Library,Author,Book
from .serializers import *
from .models import Book, Author, Library,Leads
from rest_framework import viewsets, mixins
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class LibraryListView(viewsets.GenericViewSet,
mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.DestroyModelMixin,
mixins.UpdateModelMixin):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

    def get_object(self, pk):
        try:
            return Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LibrarySerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class LibraryListView_filter(viewsets.GenericViewSet,
mixins.ListModelMixin
):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries_filter'
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class BookListView(
viewsets.GenericViewSet,
mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.UpdateModelMixin):
    paginate_by = 100
    model = Book
    context_object_name = 'books'
    serializer_class = BookSerializer
    queryset = Book.objects.all()


    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class BookListView_search(
viewsets.GenericViewSet,
mixins.ListModelMixin):
    paginate_by = 100
    model = Book
    context_object_name = 'books_search'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['title']

class AuthorListView(
viewsets.GenericViewSet,
mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.UpdateModelMixin):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AuthorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class LeadsListView(
viewsets.GenericViewSet,
mixins.CreateModelMixin):
    paginate_by = 100
    model = Leads
    context_object_name = 'leads'
    serializer_class = LeadsSerializer
    queryset = Leads.objects.all()

#book_list_view = BookListView.as_view()
#author_list_view = AuthorListView.as_view()
#library_list_view = LibraryListView.as_view()