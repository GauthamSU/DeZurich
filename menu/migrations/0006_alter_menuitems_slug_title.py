# Generated by Django 4.2.7 on 2023-12-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menuitems_slug_title_alter_menuitems_is_non_veg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='slug_title',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
