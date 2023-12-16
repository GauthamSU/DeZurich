# Generated by Django 4.2.7 on 2023-12-08 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0007_alter_menuitems_slug_title'),
        ('employee', '0006_alter_userprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('table_num', models.IntegerField(blank=True, null=True)),
                ('order_total', models.FloatField(blank=True, null=True)),
                ('order_placed', models.DateTimeField(auto_now_add=True)),
                ('order_prepared', models.DateTimeField(blank=True, null=True)),
                ('order_completed', models.DateTimeField(blank=True, null=True)),
                ('order_paid', models.DateTimeField(blank=True, null=True)),
                ('total_quantity', models.IntegerField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.userprofile')),
            ],
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
        migrations.AddField(
            model_name='orderdetails',
            name='title',
            field=models.ManyToManyField(blank=True, through='create_track_orders.OrderItem', to='menu.menuitems'),
        ),
    ]
