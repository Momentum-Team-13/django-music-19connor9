from django.contrib import admin
from django.urls import path, include
from albums import views as albums_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', albums_views.list_albums, name='list_albums'),
    path('/albums/new', albums_views.add_album, name='add_album'),
    path('/albums/<int:pk>', albums_views.album_detail, name='album_detail'),
    path("/albums/<int:pk>/edit", albums_views.edit_album, name="edit_album"),
    path("/albums/<int:pk>/delete", albums_views.delete_album, name='delete_album'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
