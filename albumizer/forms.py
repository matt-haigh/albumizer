
from django import forms

class AlbumForm(forms.Form):
    title = forms.CharField(max_length=200)
    artist = forms.CharField(max_length=200)
    rating = forms.IntegerField(required=False, min_value=1, max_value=10)
    lastfm_link = forms.CharField(max_length=200, required=False)
    rym_link = forms.CharField(max_length=200, required=False, label=u"rateyourmusic.com link")
    spotify_link = forms.CharField(max_length=200, required=False)
