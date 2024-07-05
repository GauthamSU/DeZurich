from django.core.management.base import BaseCommand
from lounge_app_services.menu.models import MenuItems
from config.env import BASE_DIR
import pandas as pd
from django.db import transaction

class Command(BaseCommand):
    help = "Generates transactions for testing"
    
    @transaction.atomic
    def handle(self, *args, **options):
        data = pd.read_csv(BASE_DIR/'menu_items.csv')
        for i in range(len(data)):
            MenuItems.objects.create(
                                        title=data['title'][i], 
                                        description=data['description'][i], 
                                        dish_image=str(data['dish_image'][i]),
                                        price=data['price'][i],
                                        is_non_veg=data['is_non_veg'][i],
                                        category=data['category'][i],
                                        sub_category=data['sub_category'][i]
                                    )
            # MenuItems.objects.filter(pk=i).update(dish_image=dish_image)
    