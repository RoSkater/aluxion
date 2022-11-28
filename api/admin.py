from django.contrib import admin

from .models import Artists, Albums, Tracks

@admin.register(Artists)
class Artist(admin.ModelAdmin):
    list_display = ('artistid', 
                    'name')
    
@admin.register(Albums)
class Album(admin.ModelAdmin):
    list_display = ('albumid',
                    'title')


@admin.register(Tracks)
class Track(admin.ModelAdmin):
    list_display = ('trackid',
                    'name')