# Generated by Django 4.2.7 on 2024-06-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]