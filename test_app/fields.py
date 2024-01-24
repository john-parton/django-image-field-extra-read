
from django.db.models.fields.files import ImageFieldFile, ImageField

class FixedImageFieldFile(ImageFieldFile):
    
    def save(self, name, content, save=True):
        name = self.field.generate_filename(self.instance, name)
        self.name = self.storage.save(name, content, max_length=self.field.max_length)
    
        # Do NOT call setattr(self.instance, self.field.name, self.name) because
        # this will call update_dimensions_field with force=True
        # The only other function of the descriptor is to set the width and height
        # fields if appropriate
        # However, the width and height fields cannot have changed in between
        # the call to the descriptors __set__ and the call to save() here
        # This avoids an extra round-trip to our storage API
        self.instance.__dict__[self.field.name] = self.name
        self._committed = True

        # Save the object because it has changed, unless save is False
        if save:
            self.instance.save()



class FixedImageField(ImageField):
    attr_class = FixedImageFieldFile
