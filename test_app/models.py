from django.db import models

from .storage import NoReadFileSystemStorage
from .fields import FixedImageField

class TestModel(models.Model):
    image = FixedImageField(
        upload_to='images/', 
        storage=NoReadFileSystemStorage(),
        width_field="width",
        height_field="height",
    )
    width = models.IntegerField()
    height = models.IntegerField()