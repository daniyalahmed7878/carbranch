# Generated by Django 5.0.6 on 2024-09-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Cars_Carousel', '0003_alter_main_cars_carousel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_cars_carousel',
            name='title_1',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='main_cars_carousel',
            name='title_2',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
