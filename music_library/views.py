from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from music_library.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the ML index.")

def artists(request):
    data = {}
    artist = Artist.objects.all().values()
    data['artist'] = list(artist)
    return JsonResponse(data)
    
def songs(request):
    data = {}
    song = Song.objects.all().values()
    data['song'] = list(song)
    return JsonResponse(data)

def genre_type(request):
    data = {}
    genre = Genre.objects.all().values()
    data['genre'] = list(genre)
    return JsonResponse(data)
