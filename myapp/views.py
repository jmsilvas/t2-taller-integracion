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
            return HttpResponse(response, content_type='application/json', status=200, reason="resultados obtenidos")
        except:
            response = json.dumps({'Error': 'failed showing artists'})
            return HttpResponse(response, content_type='application/json', status=500, reason="internal server error")
        
    elif request.method == 'POST':
        try:  
            payload = json.loads(request.body)
            id_ = b64encode(payload["name"].encode()).decode('utf-8')
            if len(id_)>22:
                id_ = id_[:22]
            try:
                artist = Artist.objects.get(ID=id_)
                response = json.dumps({'id': artist.ID,
                                'name': artist.name,
                                'age': artist.age,
                                'albums': artist.albums,
                                'tracks': artist.tracks,
                                'self': artist.myself})
                return HttpResponse(response,content_type='application/json', status=409, reason="artista ya existe")
            except:
                pass
            self_link = URL+"artists/"+id_
            artist = Artist(
                        ID=id_, 
                        name=payload["name"],
                        age=payload["age"],
                        albums= self_link+"/albums",
                        tracks= self_link+"/tracks",
                        myself= self_link  
                        )
            artist.save()
            response = json.dumps({'id': artist.ID,
                                'name': artist.name,
                                'age': artist.age,
                                'albums': artist.albums,
                                'tracks': artist.tracks,
                                'self': artist.myself})
            return HttpResponse(response, content_type='application/json', status=201, reason="artista creado")
        except:
            return HttpResponse(content_type='application/json', status=400, reason="input inválido")
       

# GET /albums: retorna todos los álbums.
def get_all_albums(request):
    if request.method == 'GET':
        album_objects = Album.objects.all()
        albums = [{'id': album.ID,
                    'artist_id': album.artist_id_id,
                    'name': album.name,
                    'genre': album.genre,
                    'artist': album.artist,
                    'tracks': album.tracks,
                    'self': album.myself} for album in album_objects]
        response = json.dumps(albums)
        return HttpResponse(response, content_type='application/json', status=200, reason="resultados obtenidos")
# GET /tracks: retorna todas las canciones.
def get_all_tracks(request):
    if request.method == 'GET':
        track_objects = Track.objects.all()
        tracks = [{'id': track.ID,
                'album_id': track.album_id_id,
                'name': track.name,
                'duration': track.duration,
                'times played': track.times_played,
                'artist': track.artist,
                'album': track.album,
                'self': track.myself} for track in track_objects]
        response = json.dumps(tracks)
        return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")

# GET /artists/<artist_id>: retorna el artista <artist_id>.
# DELETE /artists/<artist_id>: elimina el artista <artist_id> y todos sus álbums.
@csrf_exempt
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
            return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")
        except:
            return HttpResponse(content_type='application/json', status=404, reason="artista no encontrado")
    elif request.method == 'DELETE':
        try:
            artist = Artist.objects.get(ID=artist_id)
            response = json.dumps({'id': artist.ID,
                                    'name': artist.name,
                                    'age': artist.age,
                                    'albums': artist.albums,
                                    'tracks': artist.tracks,
                                    'self': artist.myself})
            artist.delete()
            return HttpResponse(response, content_type='application/json', status=204, reason="artista eliminado")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="artista inexistente")    

# GET /albums/<album_id>: retorna el álbum <album_id>.
# DELETE /albums/<album_id>: elimina el álbum <album_id> y todas sus canciones.
@csrf_exempt
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
            return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")
        except:
            return HttpResponse(content_type='application/json', status=404, reason="álbum no encontrado")  
    elif request.method == 'DELETE':
        try:
            album = Album.objects.get(ID=album_id)
            response = json.dumps({'id': album.ID,
                                    'artist_id': album.artist_id_id,
                                    'name': album.name,
                                    'genre': album.genre,
                                    'artist': album.artist,
                                    'tracks': album.tracks,
                                    'self': album.myself})
            album.delete()
            return HttpResponse(response, content_type='application/json', status=204, reason="álbum eliminado")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="álbum no encontrado") 

# GET /tracks/<track_id>: retorna la canción <track_id>.
# DELETE /tracks/<track_id>: elimina la canción <track_id>.
@csrf_exempt
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
            return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")
        except:
            return HttpResponse(content_type='application/json', status=404, reason="Canción no encontrada")
    elif request.method == 'DELETE':
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
            track.delete()
            return HttpResponse(response, content_type='application/json', status=204, reason="canción eliminada")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="canción inexistente") 
  


# GET /artists/<artist_id>/tracks: retorna todas las canciones del artista <artist_id>.
def get_artist_tracks(request, artist_id):
    if request.method == 'GET':
        try:
            track_objects = Track.objects.filter(artist=URL+"artists/"+artist_id)
            tracks = [{'id': track.ID,
                    'album_id': track.album_id_id,
                    'name': track.name,
                    'duration': track.duration,
                    'times played': track.times_played,
                    'artist': track.artist,
                    'album': track.album,
                    'self': track.myself} for track in track_objects]
            response = json.dumps(tracks)
            return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")
        except:
            return HttpResponse(response, content_type='application/json', status=404, reason="artista no encontrado")

# GET /artists/<artist_id>/albums: retorna todos los albums del artista <artist_id>.
# POST /artists/<artist_id>/albums: crea un álbum del artista <artist_id> y retorna el
#álbum creado.
@csrf_exempt
def post_album(request, artist_id):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            string = payload["name"]+":"+artist_id
            id_ = b64encode(string.encode()).decode('utf-8')
            if len(id_)>22:
                id_ = id_[:22]
            try:
                artist = Artist.objects.get(ID=artist_id)
            except:
                return HttpResponse(content_type='application/json', status=422, reason="artista no existe")
            try:
                album = Album.objects.get(ID=id_)
                response = json.dumps({'id': album.ID,
                                'artist_id': album.artist_id_id,
                                'name': album.name,
                                'genre': album.genre,
                                'artist': album.artist,
                                'tracks': album.tracks,
                                'self': album.myself})
                return HttpResponse(response, content_type='application/json', status=409, reason="álbum ya existe")
            except:
                pass
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
            album.save()
            response = json.dumps({'id': album.ID,
                                'artist_id': album.artist_id_id,
                                'name': album.name,
                                'genre': album.genre,
                                'artist': album.artist,
                                'tracks': album.tracks,
                                'self': album.myself})
            return HttpResponse(response, content_type='application/json', status=201, reason="álbum creado")
        except:
            return HttpResponse(content_type='application/json', status=400, reason="input inválido")
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
            return HttpResponse(response, content_type='application/json', status=200, reason="resultados obtenidos")
        except:
            return HttpResponse(content_type='application/json', status=404, reason="artista no encontrado")    

# GET /albums/<album_id>/tracks: retorna todas las canciones del álbum
# <album_id>.
# POST /albums/<album_id>/tracks: crea una canción del álbum <album_id> y
# retorna la canción creada.
@csrf_exempt
def post_track(request, album_id):
    if request.method == 'POST':
        try:
            try:
                album = Album.objects.get(ID=album_id)
            except:
                return HttpResponse(content_type='application/json', status=422, reason="álbum no existe")
            payload = json.loads(request.body)
            string = payload["name"]+":"+album_id
            id_ = b64encode(string.encode()).decode('utf-8')
            if len(id_)>22:
                id_ = id_[:22]  
            try:
                track = Track.objects.get(ID=id_)
                response = json.dumps({
                                'name': track.name,
                                'duration': track.duration,
                                'times played': track.times_played,
                                'artist': track.artist,
                                'album': track.album,
                                'self': track.myself})
                return HttpResponse(response, content_type='application/json', status=409, reason="canción ya existe")
            except:
                pass
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
            response = json.dumps({'id': track.ID,
                                'album_id': track.album_id_id,
                                'name': track.name,
                                'duration': track.duration,
                                'times played': track.times_played,
                                'artist': track.artist,
                                'album': track.album,
                                'self': track.myself})
            return HttpResponse(response, content_type='application/json', status=201, reason="cancion creada")
        except:
            return HttpResponse(content_type='application/json', status=400, reason="input inválido")
    elif request.method == 'GET':
        try:
            album = Album.objects.get(ID=album_id)
        except:
            return HttpResponse(content_type='application/json', status=404, reason="álbum no encontrado")
        track_objects = Track.objects.filter(album_id=album_id)
        tracks = [{'id': track.ID,
                'album_id': track.album_id_id,
                'name': track.name,
                'duration': track.duration,
                'times played': track.times_played,
                'artist': track.artist,
                'album': track.album,
                'self': track.myself} for track in track_objects]
        response = json.dumps(tracks)
        return HttpResponse(response, content_type='application/json', status=200, reason="operación exitosa")


# PUT /tracks/<track_id>/play: reproduce la canción <track_id>.
@csrf_exempt
def play_track(request, track_id):
    if request.method == 'PUT':
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
            track.times_played +=1
            response = json.dumps({'id': track.ID,
                                    'album_id': track.album_id_id,
                                    'name': track.name,
                                    'duration': track.duration,
                                    'times played': track.times_played,
                                    'artist': track.artist,
                                    'album': track.album,
                                    'self': track.myself})
            track.save()
            return HttpResponse(content_type='application/json', status=200, reason="canción reproducida")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="canción no encontrada") 

# PUT /albums/<album_id>/tracks/play: reproduce todas las canciones del álbum
# <album_id>
@csrf_exempt
def play_album_tracks(request, album_id):
    if request.method == 'PUT':
        try:
            track_objects = Track.objects.filter(album_id=album_id)
            for track in track_objects:
                track.times_played +=1
                track.save()
            return HttpResponse(content_type='application/json', status=200, reason="canciones del álbum reproducidas")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="álbum no encontrado") 

# PUT /artists/<artist_id>/albums/play
@csrf_exempt
def play_artist_tracks(request, artist_id):
    if request.method == 'PUT':
        try:
            track_objects = Track.objects.filter(artist=URL+"artists/"+artist_id)
            for track in track_objects:
                track.times_played +=1
                track.save()
            return HttpResponse(content_type='application/json', status=200, reason="todas las canciones del artista fueron reproducidas")    
        except:
            return HttpResponse(content_type='application/json', status=404, reason="artista no encontrado") 