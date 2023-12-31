from django.db import models
from django.utils.text import slugify


category_choices = (('FOOD', 'FOOD'), ('DRINKS', 'DRINKS'), ('HOOKAH', 'HOOKAH'))
subcat_choices = (('Starter', 'Starter'), ('Main Course', 'Main Course'), ('Dessert', 'Dessert'), ('Mocktail', 'Mocktail'), ('Milkshake', 'Milkshake'), ('Hot Beverages', 'Hot Beverages'), ('Hookah', 'Hookah'))

class MenuItems(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug_title = models.SlugField(unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    dish_image = models.ImageField(null=True, blank=True, upload_to='dish_images/')
    price = models.FloatField(blank=True, null=True)
    is_non_veg = models.BooleanField(default=False, blank=True, null=True)
    category = models.CharField(default='FOOD', null=True, blank=True, max_length=20, choices=category_choices)
    sub_category = models.CharField(default='Starter', null=True, blank=True, max_length=20, choices=subcat_choices)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the slug from the title before saving
        self.slug_title = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Menu items"
        verbose_name_plural = "Menu items"