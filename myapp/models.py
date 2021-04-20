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