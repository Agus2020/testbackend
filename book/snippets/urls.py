from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.db import views

urlpatterns = [
    path('snippets/', views.Library.as_view()),
    path('snippets/<int:pk>/', views.LibraryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)