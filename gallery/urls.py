

#Django
from django.conf.urls import patterns, url

urlpatterns = patterns('gallery.views',
    url(r'^image/(?P<gallery_slug>[-\w]+)/$', 'gallery_page', name='smh_gallery_gallery'),
    url(r'^video/(?P<gallery_slug>[-\w]+)/$', 'video_gallery_page', name='smh_video_gallery'),

)
