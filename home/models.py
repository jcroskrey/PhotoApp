from distutils.command.upload import upload
from tkinter import image_names
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    downloads = models.IntegerField(default=0)
    title = models.TextField(max_length=200, default='title')

    def __str__(self) -> str:
        return self.title
