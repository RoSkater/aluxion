from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from django.core import serializers

from .models import Artists, Albums, Tracks

# Create your views here.

class ArtistView(View):
    def get(self, request):
        artists = list(Artists.objects.values())
        if len(artists) > 0:
            data={'message':'Success GET','artists': artists}
        else:
            data={'message': 'GET Fail, no artists'}

        return JsonResponse(data)

class AlbumTracksView(View):
    def get(self, request):
        tracks = list(Tracks.objects.values())
        albums = list(Albums.objects.values())

        album_list = {}
        for album in albums:
            track_list = []
            track_list.clear()
            for track in tracks:
                if track['albumid_id'] == album['albumid']:
                    track_list.append(track['name'])
            album_list[album['title']] = track_list
            
        return JsonResponse(album_list)


