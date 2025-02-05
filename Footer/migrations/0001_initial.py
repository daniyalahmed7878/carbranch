# Generated by Django 5.0.6 on 2024-09-17 13:17

import Footer.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_logo', models.ImageField(upload_to='images/', validators=[Footer.models.validate_image_format])),
                ('footer_description', models.CharField(blank=True, max_length=300)),
                ('links_heading', models.CharField(blank=True, max_length=20)),
                ('link1_name', models.CharField(blank=True, max_length=15)),
                ('link1', models.CharField(blank=True, max_length=15)),
                ('link2_name', models.CharField(blank=True, max_length=15)),
                ('link2', models.CharField(blank=True, max_length=60)),
                ('link3_name', models.CharField(blank=True, max_length=15)),
                ('link3', models.CharField(blank=True, max_length=60)),
                ('link4_name', models.CharField(blank=True, max_length=15)),
                ('link4', models.CharField(blank=True, max_length=60)),
                ('contact_heading', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, help_text='Enter a valid phone number.', max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '03999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('news_letter_heading', models.CharField(blank=True, max_length=20)),
                ('facebook_link', models.CharField(blank=True, max_length=400)),
                ('twitter_link', models.CharField(blank=True, max_length=400)),
                ('youtube_link', models.CharField(blank=True, max_length=400)),
                ('whatsapp_link', models.CharField(blank=True, max_length=400)),
                ('rights', models.CharField(blank=True, max_length=200)),
                ('terms_and_conditions_link', models.CharField(blank=True, max_length=400)),
                ('privacy_policy_link', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Footer',
            },
        ),
    ]
