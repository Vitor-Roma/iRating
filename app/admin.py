from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Rating)
admin.site.register(models.Restaurant)
admin.site.register(models.Profile)
admin.site.register(models.Wishlist)