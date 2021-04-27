from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import Artist, Album, Track
from base64 import b64encode

URL = "https://murmuring-mountain-08300.herokuapp.com/"
# URL = "http://127.0.0.1:8000/"





 # GET /artists: retorna todos los artistas.
 # POST /artists: crea un artista y retorna el artista creado.
@csrf_exempt
def get_all_artists(request):
   
    if request.method == 'GET':
        try:
            artist_objects = Artist.objects.all()
            artists = [{'id': artist.ID,
                        'name': artist.name,
                        'age': artist.age,
                        'albums': artist.albums,
                        'tracks': artist.tracks,
                        'self': artist.myself} for artist in artist_objects]
            response = json.dumps(artists)
            
        except:
            response = json.dumps({'Error': 'failed showing artists'})
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
        album_objects = Album.objects.all()
        try:
            albums = [{'id': album.ID,
                        'artist_id': album.artist_id_id,
                        'name': album.name,
                        'genre': album.genre,
                        'artist': album.artist,
                        'tracks': album.tracks,
                        'self': album.myself} for album in album_objects]
            response = json.dumps(albums)
        except:
            response = json.dumps({'Error': 'No album with that id'})
        return HttpResponse(response, content_type='application/json')
## fix 'Album' object has no attribute 'album_id_id' cuando esta vacia
# GET /tracks: retorna todas las canciones.
def get_all_tracks(request):
    if request.method == 'GET':
        track_objects = Track.objects.all()
      
        try:
            tracks = [{'id': track.ID,
                    'album_id': track.album_id_id,
                    'name': track.name,
                    'duration': track.duration,
                    'times played': track.times_played,
                    'artist': track.artist,
                    'album': track.album,
                    'self': track.myself} for track in track_objects]
            response = json.dumps(tracks)
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
                                    'artist_id': album.artist_id_id,
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
                                    'album_id': track.album_id_id,
                                    'name': track.name,
                                    'duration': track.duration,
                                    'times played': track.times_played,
                                    'artist': track.artist,
                                    'album': track.album,
                                    'self': track.myself})
        except:
            response = json.dumps({'Error': 'No track with that id'})
        return HttpResponse(response, content_type='application/json')


# GET /artists/<artist_id>/tracks: retorna todas las canciones del artista <artist_id>.
def get_artist_tracks(request, artist_id):
    if request.method == 'GET':
        track_objects = Track.objects.filter(artist=URL+"artists/"+artist_id)
        print(len(track_objects))
        tracks = [{'id': track.ID,
                    'album_id': track.album_id_id,
                    'name': track.name,
                    'duration': track.duration,
                    'times played': track.times_played,
                    'artist': track.artist,
                    'album': track.album,
                    'self': track.myself} for track in track_objects]
        response = json.dumps(tracks)
        try:
            print("hello")
        except:
            response = json.dumps({'Error': 'No track with that id'})
        return HttpResponse(response, content_type='application/json')


# GET /artists/<artist_id>/albums: retorna todos los albums del artista <artist_id>.
# POST /artists/<artist_id>/albums: crea un álbum del artista <artist_id> y retorna el
#álbum creado.
# fix: titulos muy largos
@csrf_exempt
def post_album(request, artist_id):
    if request.method == 'POST':
        payload = json.loads(request.body)
        id_ = b64encode(payload["name"].encode()).decode('utf-8')
        album_link = URL+"albums/"+id_
        album = Album(
                        ID = id_,
                        artist_id = Artist.objects.get(ID=artist_id),
                        name = payload["name"],
                        genre = payload["genre"],
                        artist = URL+"artists/"+artist_id,
                        tracks = album_link+"/tracks",
                        myself = album_link
                        )
        try:
            album.save()
            response = json.dumps([{"success": "album created"}])
        except:
            response = json.dumps([{"Error": "something went wrong"}])
    elif request.method == 'GET':
        album_objects = Album.objects.filter(artist_id=artist_id)
        try:
            albums = [{'id': album.ID,
                    'artist_id': album.artist_id_id,
                    'name': album.name,
                    'genre': album.genre,
                    'artist': album.artist,
                    'tracks': album.tracks,
                    'self': album.myself} for album in album_objects]
            response = json.dumps(albums)
        except:
            response = json.dumps({'Error': 'No album with that id'})
    return HttpResponse(response, content_type='application/json')

# GET /albums/<album_id>/tracks: retorna todas las canciones del álbum
# <album_id>.
# POST /albums/<album_id>/tracks: crea una canción del álbum <album_id> y
# retorna la canción creada.
@csrf_exempt
def post_track(request, album_id):
    if request.method == 'POST':
        payload = json.loads(request.body)
        id_ = b64encode(payload["name"].encode()).decode('utf-8')
        album = Album.objects.get(ID=album_id)
        artist = Artist.objects.get(ID=album.artist_id.ID)
        track = Track(
                        ID = id_,
                        album_id = album,
                        name = payload["name"],
                        duration = payload["duration"],
                        times_played = 0,
                        artist = URL+"artists/"+artist.ID,
                        album = URL+"albums/"+album.ID,
                        myself = URL+"tracks/"+id_
                        )
        track.save()    
        try:
        
            response = json.dumps([{"success": "track created"}])
        except:
            response = json.dumps([{"Error": "something went wrong"}])
    elif request.method == 'GET':
        track_objects = Track.objects.filter(album_id=album_id)
        try:
            tracks = [{'id': track.ID,
                    'album_id': track.album_id_id,
                    'name': track.name,
                    'duration': track.duration,
                    'times played': track.times_played,
                    'artist': track.artist,
                    'album': track.album,
                    'self': track.myself} for track in track_objects]
            response = json.dumps(tracks)
        except:
            response = json.dumps({'Error': 'No track with that id'})
    return HttpResponse(response, content_type='application/json')