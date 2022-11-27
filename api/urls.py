from django.urls import path

from .views import ArtistView, AlbumTracksView

urlpatterns = [
    path('artists/', ArtistView.as_view(), name='artists_list'),
    path('albums/', AlbumTracksView.as_view(), name='albums_tracks_list'),
]