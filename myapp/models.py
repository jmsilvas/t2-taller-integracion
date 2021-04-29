from django.db import models


# Cada artista debe tener los siguientes atributos:
# ID. (string)
# Name. (string)
# Age. (int)
# Albums. (url) 5
# Tracks. (url) 6
# Self. (url) 7
class Artist(models.Model):
    ID = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    albums = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()

# Cada álbum debe tener los siguientes atributos:
# ID. (string)
# Name. (string)
# Genre. (string)
# Artist. (url)
# Tracks. (url)
# Self. (url)

class Album(models.Model):
    ID = models.CharField(max_length=30, primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    artist = models.URLField()
    tracks = models.URLField()
    myself = models.URLField()

# Finalmente, cada canción debe tener los siguientes atributos:
# ID. (string)
# Name. (string)
# Duration. (float) 8
# Times Played. (int)
# Artist. (url)
# Album. (url)
# Self. (url)
class Track(models.Model):
    ID = models.CharField(max_length=30, primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    duration = models.FloatField()
    times_played = models.IntegerField()
    artist = models.URLField()
    album = models.URLField()
    myself = models.URLField()
