# Generated by Django 5.0.6 on 2024-08-16 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_car_image_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Comment',
        ),
    ]
