# Generated by Django 5.0.6 on 2024-09-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Header', '0007_alter_header_header_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='dropdownlinks_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
