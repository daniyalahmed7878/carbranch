# Generated by Django 5.0.6 on 2024-09-16 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Header', '0004_header_notes_alter_header_link1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='notes',
        ),
    ]
