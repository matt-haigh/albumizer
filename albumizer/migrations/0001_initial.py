# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Album'
        db.create_table('albumizer_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('lastfm_link', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('rym_link', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('spotify_link', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('albumizer', ['Album'])

        # Adding unique constraint on 'Album', fields ['title', 'artist']
        db.create_unique('albumizer_album', ['title', 'artist'])

    def backwards(self, orm):
        
        # Removing unique constraint on 'Album', fields ['title', 'artist']
        db.delete_unique('albumizer_album', ['title', 'artist'])

        # Deleting model 'Album'
        db.delete_table('albumizer_album')

    models = {
        'albumizer.album': {
            'Meta': {'unique_together': "(('title', 'artist'),)", 'object_name': 'Album'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastfm_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'rym_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'spotify_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['albumizer']
