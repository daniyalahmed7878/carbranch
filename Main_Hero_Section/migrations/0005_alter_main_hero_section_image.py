# Generated by Django 5.0.6 on 2024-08-03 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Hero_Section', '0004_alter_main_hero_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_hero_section',
            name='image',
            field=models.FileField(max_length=200, null=True, upload_to='Main-Hero-Section/'),
        ),
    ]
