from django.db import models

# Create your models here.
class MenuItems(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    dish_image = models.ImageField(null=True, blank=True, upload_to='dish_images/')
    price = models.FloatField(blank=True, null=True)
    is_non_veg = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title