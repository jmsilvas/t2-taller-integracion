"""RestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists', views.get_all_artists),
    path('albums', views.get_all_albums),
    path('tracks', views.get_all_tracks),
    path('artists/<str:artist_id>', views.get_artist),
    path('artists/<str:artist_id>/albums', views.post_album),
    path('artists/<str:artist_id>/tracks', views.get_artist_tracks),
    # /artists/<artist_id>/tracks:
    path('albums/<str:album_id>', views.get_album),
    path('albums/<str:album_id>/tracks', views.post_track),
    path('tracks/<str:track_id>', views.get_track)
]
