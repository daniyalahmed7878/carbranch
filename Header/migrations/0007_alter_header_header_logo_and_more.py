# Generated by Django 5.0.6 on 2024-09-16 21:59

import Header.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Header', '0006_alter_header_header_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='header_logo',
            field=models.ImageField(upload_to='images/', validators=[Header.models.validate_image_format]),
        ),
        migrations.AlterField(
            model_name='header',
            name='side_navigation_image',
            field=models.ImageField(upload_to='images/', validators=[Header.models.validate_image_format]),
        ),
    ]
