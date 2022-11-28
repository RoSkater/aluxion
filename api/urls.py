from django.urls import path

from .views import ArtistView, AlbumTracksView, AlbumArtistTracks

urlpatterns = [
    path('artists/', ArtistView.as_view(), name='artists_list'),
    path('albums/', AlbumTracksView.as_view(), name='albums_tracks_list'),
    path('artists/<str:name>', ArtistView.as_view(), name='artist_albums_tracks_list'),
    path('albums/<str:title>', AlbumTracksView.as_view(), name='certain_album_tracks_list'),
    path('album_artist/', AlbumArtistTracks.as_view(), name='album_artist_tracks_num')
]