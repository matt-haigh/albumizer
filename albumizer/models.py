from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    
    rating = models.PositiveIntegerField(null=True)
    
    lastfm_link = models.CharField(max_length=200, blank=True)
    rym_link = models.CharField(max_length=200, blank=True)
    spotify_link = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('title', 'artist')