from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    
    url(r'^$', 'albumizer.views.home'),
    url(r'^add/$', 'albumizer.views.add_album'),
    url(r'^album/(?P<album_id>[\d]+)/$', 'albumizer.views.view_album'),
    url(r'^pick/$', 'albumizer.views.pick'),
    
)
