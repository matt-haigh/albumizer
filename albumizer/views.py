from random import randint

from django.db import transaction
from django.shortcuts import redirect, render

from albumizer.forms import AlbumForm
from albumizer.models import Album

def bulk_add_albums(album_data):
    for a in album_data:
        if Album.objects.filter(title=a["album"], artist=a["artist"]).exists():
            continue
        Album.objects.create(
            artist=a["artist"],
            title=a["album"],
            lastfm_link=a["link"])


@transaction.commit_on_success
def home(request):
    return render(request, "home.html")


@transaction.commit_on_success
def add_album(request):
    if request.method == "POST" and "add_album_submit" in request.POST.keys():
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            data = album_form.cleaned_data
            album = Album.objects.create(
                artist=data["artist"],
                title=data["title"],
                rating=data["rating"],
                lastfm_link=data["lastfm_link"],
                rym_link=data["rym_link"],
                spotify_link=data["spotify_link"])
            return redirect(view_album, album_id=album.id)
    else:
        album_form = AlbumForm()
    
    return render(request, "add_album.html", {
        "form": album_form})


@transaction.commit_on_success
def view_album(request, album_id):
    album = Album.objects.get(id=album_id)
    
    # Create an album form using the existing album's data
    album_form = AlbumForm(initial={
        "artist": album.artist,
        "title": album.title,
        "rating": album.rating,
        "lastfm_link": album.lastfm_link,
        "rym_link": album.rym_link,
        "spotify_link": album.spotify_link})
    
    # Handle album update
    if request.method == "POST" and "update_album_submit" in request.POST.keys():
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            data = album_form.cleaned_data
            album.artist = data["artist"]
            album.title = data["title"]
            album.rating = data["rating"]
            album.lastfm_link=data["lastfm_link"]
            album.rym_link=data["rym_link"]
            album.spotify_link=data["spotify_link"]
            album.save()

    return render(request, "view_album.html", {
        "album": album,
        "album_form": album_form})


@transaction.commit_on_success
def pick(request):
    album_count = Album.objects.all().count()
    
    if not album_count:
        return redirect(home)
    
    rand = randint(1, album_count)
    return redirect(view_album, album_id=rand)
    