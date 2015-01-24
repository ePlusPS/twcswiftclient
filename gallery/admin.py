from gallery.models import Gallery, Image, Video
from django.contrib import admin

class GalleryAdmin(admin.ModelAdmin):
    fields = ('name','description')
    list_display = ('name', 'slug')

admin.site.register(Gallery, GalleryAdmin)


class ImageAdmin(admin.ModelAdmin):
    fields = ('name','image','description','date','gallery')
    list_display = ('name','image')
    list_filter = ('gallery',)

admin.site.register(Image, ImageAdmin)

class VideoAdmin(admin.ModelAdmin):
    fields = ('name','video','description','date','gallery')
    list_display = ('name','video')
    list_filter = ('gallery',)

admin.site.register(Video, VideoAdmin)
