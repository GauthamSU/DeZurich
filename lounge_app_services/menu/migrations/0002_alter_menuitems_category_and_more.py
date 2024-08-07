# Generated by Django 4.2.7 on 2024-06-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='category',
            field=models.CharField(blank=True, choices=[('FOOD', 'FOOD'), ('DRINKS', 'DRINKS'), ('DESSERT', 'DESSERT'), ('HOOKAH', 'HOOKAH')], default='FOOD', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('Mocktail & Mojito', 'Mocktail & Mojito'), ('Milkshake', 'Milkshake'), ('Frappuccino', 'Frappuccino'), ('Soft drinks', 'Soft Drinks'), ('Hot Beverages', 'Hot Beverages'), ('Soup', 'Soup'), ('Salad', 'Salad'), ('Lasagna', 'Lasagna'), ('Starters', 'Starters'), ('Burger', 'Burger'), ('Pizza', 'Pizza'), ('Sandwich', 'Sandwich'), ('Grill', 'From the Grill'), ('Pasta', 'Pasta'), ('Rice', 'Rice'), ('Ice Cream', 'Ice Cream'), ('Dessert', 'Dessert')], default='Starter', max_length=20, null=True),
        ),
    ]
