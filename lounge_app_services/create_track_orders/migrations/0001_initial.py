# Generated by Django 4.2.7 on 2024-06-06 08:47

from django.db import migrations, models
import django.db.models.deletion
import lounge_app_services.create_track_orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=lounge_app_services.create_track_orders.models.id_generator, max_length=6, null=True, unique=True)),
                ('table_num', models.IntegerField(blank=True, null=True)),
                ('order_total', models.FloatField(blank=True, null=True)),
                ('order_placed', models.DateTimeField(auto_now_add=True)),
                ('order_prepared', models.DateTimeField(blank=True, null=True)),
                ('order_completed', models.DateTimeField(blank=True, null=True)),
                ('order_paid', models.DateTimeField(blank=True, null=True)),
                ('total_quantity', models.IntegerField(blank=True, null=True)),
                ('order_status', models.CharField(blank=True, choices=[('order_placed', 'Order Placed'), ('order_prepared', 'Order Prepared'), ('order_completed', 'Order Completed'), ('order_paid', 'Order Paid')], default='order_placed', max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Order details',
                'verbose_name_plural': 'Order details',
                'ordering': ['-order_placed'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('preference', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('order_price', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_track_orders.orderdetails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitems')),
            ],
        ),
    ]