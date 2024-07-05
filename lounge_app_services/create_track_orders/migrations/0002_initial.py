# Generated by Django 4.2.7 on 2024-06-06 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('create_track_orders', '0001_initial'),
        ('menu', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.userprofile'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='title',
            field=models.ManyToManyField(blank=True, through='create_track_orders.OrderItem', to='menu.menuitems'),
        ),
    ]
