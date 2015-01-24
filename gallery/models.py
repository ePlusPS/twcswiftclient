
from django.db import models
from django.template.defaultfilters import slugify

import thumbs
from swift.storage import SwiftStorage

swift = SwiftStorage()

class Gallery(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "galleries"

    def __unicode__(self):
        return(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs) # Call the "real" save() method.


class Image(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='Image_Repo')
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    gallery = models.ForeignKey(Gallery)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return(self.name)
    
    def delete(self):
		swift.delete(self.image.name)
		super(Image, self).delete()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs) # Call the "real" save() method.


class Video(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name =  models.CharField(max_length=50)
    video = models.FileField(upload_to='Video_Repo',null=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    gallery = models.ForeignKey(Gallery)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return(self.name)
    
    def delete(self):
		swift.delete(self.video.name)
		super(Video, self).delete()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Video, self).save(*args, **kwargs) # Call the "real" save() method.

