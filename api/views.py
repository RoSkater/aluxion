from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from .models import Artists, Albums, Tracks

# Create your views here.

def getAlbumwithTracks(albums, tracks):
    # Get Album Name with all its tracks

    album_list = {}
    for album in albums:
        track_list = []
        track_list.clear()
        for track in tracks:
            if track['albumid_id'] == album['albumid']:
                track_list.append(track['name'])
        album_list[album['title']] = track_list
    return album_list

def nameAdjustment(name):
    # Adapt URL Syntax to names with '/' and spaces

    name = name.replace('-','/')
    name = name.replace('_',' ')
    return name

class ArtistView(View):
    def get(self, request, name=None):

        if name:
            name = nameAdjustment(name)

            artist = list(Artists.objects.filter(name=name).values())
            tracks = list(Tracks.objects.values())
            albums = list(Albums.objects.filter(artistid=artist[0]['artistid']).values())

            data = getAlbumwithTracks(albums, tracks)

            if artist[0]['artistid'] > 0:
                data = data={'message':'Success GET individual','artist': name,'data': data}

            else:
                data={'message': 'GET Fail, no artist with that name', 'artist': name}

        else:
            artists = list(Artists.objects.values())

            if len(artists) > 0:
                data={'message':'Success GET','artists': artists}
            else:
                data={'message': 'GET Fail, no artists'}

        return JsonResponse(data)

class AlbumTracksView(View):
    def get(self, request, title=None):
        
        if title:
            title = nameAdjustment(title)
            albums = list(Albums.objects.filter(title=title).values())

        else:
            albums = list(Albums.objects.values())

        tracks = list(Tracks.objects.values())
            
        return JsonResponse(getAlbumwithTracks(albums, tracks))

class AlbumArtistTracks(View):
    def get(self, request):
        albums = list(Albums.objects.values())
        tracks = list(Tracks.objects.values())

        lista = getAlbumwithTracks(albums, tracks)

        data = {}

        for album_name in lista:
            track_num = len(lista[album_name])

            for album in albums:
                if album['title'] == album_name:
                   artist_list = list(Artists.objects.filter(artistid=album['artistid_id']).values())
                   artist = artist_list[0]['name']

            data.update({album_name : {'Number of tracks': track_num, 'Artist': artist}})

        
        return JsonResponse(data)