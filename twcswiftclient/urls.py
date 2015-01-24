from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'gallery.views.static_section', name='home'),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<section>[-\w]+)/$', 'gallery.views.static_section', name='static_section'),
)
