# Generated by Django 5.0.6 on 2024-09-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARS', '0006_alter_cars_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]

