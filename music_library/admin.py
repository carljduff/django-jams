from django.contrib import admin
from music_library.models import *
# Register your models here.

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Genre)