from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # music_library/''
    path('artist/', views.artists), # music_library/artist/
    path('song/', views.songs), # music_library/song/
    path('genre/', views.genre_type) #music_library/genre/
]