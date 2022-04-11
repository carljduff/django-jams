from django.db import models

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=500)
    duration = models.IntegerField()
    artist_name = models.CharField(max_length=200, blank=False, null=False)
    genre = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) #many-to-one... one artist can have many songs

    def __str__(self):
        return self.title and self.artist_name