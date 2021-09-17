from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from book.views import BookListView,AuthorListView,LibraryListView,LeadsListView


router = DefaultRouter()
router.register('book',BookListView)
router.register('author',AuthorListView)
router.register('library',LibraryListView)
router.register('leads',LeadsListView)

urlpatterns = router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
    
]