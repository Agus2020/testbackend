from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from book.views import BookListView,AuthorListView,LibraryListView,LeadsListView


router = DefaultRouter()
router.register('api/book',BookListView)
router.register('api/author',AuthorListView)
router.register('api/library',LibraryListView)
router.register('api/leads',LeadsListView)

urlpatterns = router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
    
]