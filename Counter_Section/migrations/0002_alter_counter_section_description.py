# Generated by Django 5.0.6 on 2024-08-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counter_Section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter_section',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
