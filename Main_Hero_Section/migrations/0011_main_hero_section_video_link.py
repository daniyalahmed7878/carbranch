# Generated by Django 5.0.6 on 2024-09-02 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Hero_Section', '0010_alter_main_hero_section_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_hero_section',
            name='video_link',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
