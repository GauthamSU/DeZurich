# Generated by Django 4.2.7 on 2023-12-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitems_is_non_veg'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitems',
            name='category',
            field=models.CharField(blank=True, choices=[('FOOD', 'FOOD'), ('DRINKS', 'DRINKS'), ('HOOKAH', 'HOOKAH')], default='FOOD', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='dish_image',
            field=models.ImageField(blank=True, null=True, upload_to='dish_images/'),
        ),
    ]
