from django.db import models

from .storage import NoReadFileSystemStorage

class TestModel(models.Model):
    image = models.ImageField(
        upload_to='images/', 
        storage=NoReadFileSystemStorage(),
    )
    width = models.IntegerField()
    height = models.IntegerField()