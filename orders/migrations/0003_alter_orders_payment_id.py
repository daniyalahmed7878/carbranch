# Generated by Django 5.0.6 on 2024-09-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_options_orders_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
