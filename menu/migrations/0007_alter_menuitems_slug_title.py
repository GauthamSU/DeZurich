# Generated by Django 4.2.7 on 2023-12-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_menuitems_slug_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='slug_title',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]