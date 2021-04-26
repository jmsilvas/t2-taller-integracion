from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import Artist, Album, Track
from base64 import b64encode

URL = "https://murmuring-mountain-08300.herokuapp.com/"


## GET

@csrf_exempt
def get_all_artists(request):
    # GET /artists: retorna todos los artistas.
    if request.method == 'GET':
        try:
            artist_objects = Artist.objects.all()
            artists = [{'id': artist.ID,
                        'name': artist.name,
                        'age': artist.age,
                        'albums': artist.albums,
                        'tracks': artist.tracks,
                        'self': artist.myself} for artist in artist_objects]
            print(artists)

            response = json.dumps(artists)
            
        except:
            response = json.dumps({'Error': 'failed showing artists'})
    # POST /artists: crea un artista y retorna el artista creado.
    elif request.method == 'POST':
        payload = json.loads(request.body)
        id_ = b64encode(payload["name"].encode()).decode('utf-8')
        self_link = URL+"artists/"+id_
        artist = Artist(
                        ID=id_, 
                        name=payload["name"],
                        age=payload["age"],
                        albums= self_link+"/albums",
                        tracks= self_link+"/tracks",
                        myself= self_link  
                        )
        try:
            artist.save()
            response = json.dumps([{"success": "artist created"}])
        except:
            response = json.dumps([{"Error": "something went wrong"}])
    return HttpResponse(response, content_type='application/json')



# GET /albums: retorna todos los álbums.
def get_all_albums(request):
    if request.method == 'GET':
        try:
            album = Album.objects.get()
            response = json.dumps([{'id': album.ID,
                                    'artist_id': album.artist_id,
                                    'name': album.name,
                                    'genre': album.genre,
                                    'artist': album.artist,
                                    'tracks': album.tracks,
                                    'self': album.myself}])
        except:
            response = json.dumps({'Error': 'No album with that id'})
        return HttpResponse(response, content_type='application/json')
# GET /tracks: retorna todas las canciones.
def get_all_tracks(request):
    if request.method == 'GET':
        try:
            track = Track.objects.get()
            response = json.dumps([{'id': track.ID,
                                    'album_id': track.album_id,
                                    'name': track.name,
                                    'duration': track.duration,
                                    'times played': track.times_played,
                                    'artist': track.artist,
                                    'tracks': track.tracks,
                                    'self': track.myself}])
        except:
            response = json.dumps({'Error': 'No track with that id'})
        return HttpResponse(response, content_type='application/json')




# GET /artists/<artist_id>: retorna el artista <artist_id>.
def get_artist(request, artist_id):
    if request.method == 'GET':
        try:
            artist = Artist.objects.get(ID=artist_id)
            response = json.dumps({'id': artist.ID,
                                    'name': artist.name,
                                    'age': artist.age,
                                    'albums': artist.albums,
                                    'tracks': artist.tracks,
                                    'self': artist.myself})
        except:
            response = json.dumps({'Error': 'No artist with that id'})
        return HttpResponse(response, content_type='application/json')

# GET /albums/<album_id>: retorna el álbum <album_id>.
def get_album(request, album_id):
    if request.method == 'GET':
        try:
            album = Album.objects.get(ID=album_id)
            response = json.dumps({'id': album.ID,
                                    'artist_id': album.artist_id,
                                    'name': album.name,
                                    'genre': album.genre,
                                    'artist': album.artist,
                                    'tracks': album.tracks,
                                    'self': album.myself})
        except:
            response = json.dumps({'Error': 'No album with that id'})
        return HttpResponse(response, content_type='application/json')

# GET /tracks/<track_id>: retorna la canción <track_id>.
def get_track(request, track_id):
    if request.method == 'GET':
        try:
            track = Track.objects.get(ID=track_id)
            response = json.dumps({'id': track.ID,
                                    'album_id': track.album_id,
                                    'name': track.name,
                                    'duration': track.duration,
                                    'times played': track.times_played,
                                    'artist': track.artist,
                                    'tracks': track.tracks,
                                    'self': track.myself})
        except:
            response = json.dumps({'Error': 'No track with that id'})
        return HttpResponse(response, content_type='application/json')


## POST

# POST /artists/<artist_id>/albums: crea un álbum del artista <artist_id> y retorna el
#álbum creado.
# POST /albums/<album_id>/tracks: crea una canción del álbum <album_id> y
# retorna la canción creada.