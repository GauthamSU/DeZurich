from django.contrib import admin
from .models import MenuItems

# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'sub_category', 'is_non_veg', 'price']

admin.site.register(MenuItems, MenuItemsAdmin)