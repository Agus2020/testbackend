from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from book.views import *


router = DefaultRouter()
router.register('api/book',BookListView,basename="books")
router.register('api/book_search',BookListView_search)
router.register('api/library',LibraryListView,basename="libraries")
router.register('api/library_filter',LibraryListView_filter)
router.register('api/author',AuthorListView)
router.register('api/leads',LeadsListView)

urlpatterns = router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
    
]