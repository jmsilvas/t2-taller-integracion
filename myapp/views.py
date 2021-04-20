from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.models import Artist

def get_artist(request, artist_id):
    if request.method == 'GET':
        try:
            artist = Artist.objects.get(ID=artist_id)
            response = json.dumps({'ID': artist.ID,
                                    'name': artist.name,
                                    'age': artist.age,
                                    'albums': artist.albums,
                                    'tracks': artist.tracks,
                                    'self': artist.myself})
        except:
            response = json.dumps({'Error': 'No artist with that id'})
        return HttpResponse(response, content_type='application/json')