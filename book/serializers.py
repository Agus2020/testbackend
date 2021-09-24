from rest_framework import serializers
from .models import *

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class LibrarySerializer_filter(serializers.ModelSerializer):
    class Meta:
        model = Library_filter
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.last_name') 
    libraries = LibrarySerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class BookSerializer_search(serializers.ModelSerializer):
    author = serializers.CharField(source='author.last_name') 
    libraries = LibrarySerializer(many=True)
    class Meta:
        model = Book_search
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'         