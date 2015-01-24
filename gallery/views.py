
#Django libs
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.http import Http404

from gallery.models import Gallery, Image, Video

#View for a gallery
def gallery_page(request, gallery_slug):
    gallery = Gallery.objects.get_or_create(name = gallery_slug)
    if gallery:
		gallery = Gallery.objects.get(name = gallery_slug)
    images = Image.objects.filter(gallery=gallery_slug).order_by('-date')
    section = gallery_slug
    return (render(request, 'gallery.html', locals()))


#View for a gallery item
def image_page(request, gallery_slug, image_slug):
    gallery = get_object_or_404(Gallery, slug=gallery_slug)  #Check for correct url
    image = get_object_or_404(Image, slug=image_slug)
    section = gallery_slug
    permalink = request.build_absolute_uri()
    return (render(request, 'image.html', locals()))
    
#View for a gallery
def video_gallery_page(request, gallery_slug):
    gallery = Gallery.objects.get_or_create(name = gallery_slug)
    if gallery:
		gallery = Gallery.objects.get(name = gallery_slug)
    videos = Video.objects.filter(gallery=gallery_slug).order_by('-date')
    section = gallery_slug
    return (render(request, 'video_gallery.html', locals()))


#View for a gallery item
def video_page(request, gallery_slug, video_slug):
    gallery = get_object_or_404(Gallery, slug=gallery_slug)  #Check for correct url
    video = get_object_or_404(Video, slug=video_slug)
    section = gallery_slug
    permalink = request.build_absolute_uri()
    return (render(request, 'video.html', locals()))

def static_section(request, section="home"):
    section = section
    try:
        return (render(request, '{section}.html'.format(section=section), locals()))
    except TemplateDoesNotExist:
        raise Http404
