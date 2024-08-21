# Generated by Django 5.0.6 on 2024-08-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank='True', null='True', upload_to='')),
                ('brands', models.ManyToManyField(to='brands.brand')),
            ],
        ),
    ]
