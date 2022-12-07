from django.contrib import admin
from .models import Photo, ProfilePhoto
from imagekit.admin import AdminThumbnail
from imagekit.cachefiles import ImageCacheFile
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill



class PhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image_display', 'downloads']
    readonly_fields = ['image_tag']
    image_display = AdminThumbnail(image_field='image_small')
    image_display.short_description = 'Image'


class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image_display']
    readonly_fields = ['image_tag']
    image_display = AdminThumbnail(image_field='image_small')
    image_display.short_description = 'Image'

admin.site.register(Photo, PhotoAdmin)
admin.site.register(ProfilePhoto, ProfilePhotoAdmin)