# Generated by Django 5.0.6 on 2024-08-13 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CARS', '0003_alter_cars_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='title',
            new_name='name',
        ),
    ]

