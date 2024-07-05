from django.db import models
from django.utils.text import slugify


CATEGORY_CHOICES = (('FOOD', 'FOOD'), ('DRINKS', 'DRINKS'), ('DESSERT', 'DESSERT'), ('HOOKAH', 'HOOKAH'))

DRINKS_SUBCAT_CHOICES = (
    ('Mocktail & Mojito', 'Mocktail & Mojito'), 
    ('Milkshake', 'Milkshake'),
    ('Frappuccino', 'Frappuccino'),
    ('Hot Beverages', 'Hot Beverages'),
    ('Soft Drinks', 'Soft drinks')
    )

FOOD_SUBCAT_CHOICES = (
    ('Soup', 'Soup'),
    ('Salad', 'Salad'),
    ('Lasagna', 'Lasagna'),
    ('Pasta', 'Pasta'),
    ('Burger', 'Burger'),
    ('Pizza', 'Pizza'),
    ('Sandwich', 'Sandwich'),
    ('Grill', 'From the Grill'),
    ('Rice', 'Rice'),
    ('Starters', 'Starters')
)

DESSERT_SUBCAT_CHOICES = (
    ('Ice Cream', 'Ice Cream'), 
    ('Dessert', 'Dessert')
)

SUBCAT_CHOICES = DRINKS_SUBCAT_CHOICES + FOOD_SUBCAT_CHOICES + DESSERT_SUBCAT_CHOICES

class MenuItems(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug_title = models.SlugField(unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    dish_image = models.ImageField(null=True, blank=True, upload_to='dish_images/')
    price = models.FloatField(blank=True, null=True)
    is_non_veg = models.BooleanField(default=False, blank=True, null=True)
    category = models.CharField(default='FOOD', null=True, blank=True, max_length=20, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(default='Starter', null=True, blank=True, max_length=20, choices=SUBCAT_CHOICES)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the slug from the title before saving
        self.slug_title = slugify(self.title + ' ' + str(self.sub_category) + ' ' + str(self.is_non_veg))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Menu items"
        verbose_name_plural = "Menu items"