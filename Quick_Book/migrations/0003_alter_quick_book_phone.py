# Generated by Django 5.0.6 on 2024-09-09 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quick_Book', '0002_remove_quick_book_pickupdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quick_book',
            name='phone',
            field=models.CharField(help_text='Enter a valid phone number.', max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '03999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
