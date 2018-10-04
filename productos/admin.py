from django.contrib import admin

from .models import Producto

from image_cropping import ImageCroppingMixin

class ProductoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Producto, ProductoAdmin)
