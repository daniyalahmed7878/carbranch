# Generated by Django 5.0.6 on 2024-09-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quick_Book', '0003_alter_quick_book_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quick_book',
            name='car',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
