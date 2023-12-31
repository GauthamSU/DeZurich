# Generated by Django 4.2.7 on 2023-11-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('DNS', 'Do not want to specify')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
