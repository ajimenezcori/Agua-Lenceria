from django.db import models
from image_cropping import ImageRatioField

# Create your models here.

class Producto(models.Model):
    imagen = models.ImageField(blank=True, upload_to='productos')
    # size is "width x height"
    cropping = ImageRatioField('imagen', '400x400')
    nombre = models.CharField(max_length = 180)
    precio= models.IntegerField()

    def __str__(self):
        return (self.nombre+' : '+str(self.precio))
