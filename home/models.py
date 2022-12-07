from distutils.command.upload import upload
from django.db import models
from django.utils.html import mark_safe
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Photo(models.Model):
    image = models.ImageField()  # Save in default MEDIA_ROOT loc defined in settings.py
    downloads = models.IntegerField(default=0)
    title = models.TextField(max_length=200, default='title')
    image_small = ProcessedImageField(processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60},
                                    )

    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.image}" width="300" height="200"/>')

    def __str__(self) -> str:
        return self.title
    image_tag.short_description = 'Image'


class ProfilePhoto(models.Model):
    image = models.ImageField()
    # image_small for admin page
    image_small = ProcessedImageField(processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60},
                                    )

    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.image}" width="300" height="200"/>')

    image_tag.short_description = 'Image'

    # def image_tag(self):
    #     return mark_safe(f'<img src="./home/photos/{self.image}" width="150" height="150"/>')
    
    # image_tag.short_description = 'Image'