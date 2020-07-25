from django.db import models
from meta.models import ModelMeta

class MyModel(ModelMeta, models.Model):
    name = models.CharField(max_length=20)
    abstract = models.TextField()
    image = models.ImageField()
    ...

    _metadata = {
        'title': 'name',
        'description': 'abstract',
        'image': 'get_meta_image',
        ...
    }
    def get_meta_image(self):
        if self.image:
            return self.image.url