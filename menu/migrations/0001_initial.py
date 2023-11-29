# Generated by Django 4.2.7 on 2023-11-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('dish_image', models.ImageField(blank=True, default='profile.png', null=True, upload_to='dish_images/')),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
