# Generated by Django 5.0.6 on 2024-08-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('image', models.FileField(max_length=200, null=True, upload_to='Cars/')),
                ('new_car', models.CharField(blank=True, max_length=60, null=True)),
                ('passengers', models.CharField(max_length=60, null=True)),
                ('price', models.CharField(max_length=60, null=True)),
                ('petrol_diesel', models.CharField(blank=True, max_length=60, null=True)),
                ('automatic_manual', models.CharField(blank=True, max_length=60, null=True)),
                ('at_mt', models.CharField(blank=True, max_length=60, null=True)),
                ('car_image_1', models.FileField(blank=True, max_length=200, null=True, upload_to='Cars/')),
                ('car_image_2', models.FileField(blank=True, max_length=200, null=True, upload_to='Cars/')),
                ('car_image_3', models.FileField(blank=True, max_length=200, null=True, upload_to='Cars/')),
                ('car_image_4', models.FileField(blank=True, max_length=200, null=True, upload_to='Cars/')),
                ('rating_per', models.CharField(blank=True, max_length=60, null=True)),
                ('reviews', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('feature_1', models.CharField(blank=True, max_length=60, null=True)),
                ('feature_2', models.CharField(blank=True, max_length=60, null=True)),
                ('feature_3', models.CharField(blank=True, max_length=60, null=True)),
                ('feature_4', models.CharField(blank=True, max_length=60, null=True)),
                ('feature_5', models.CharField(blank=True, max_length=60, null=True)),
                ('feature_6', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'OUR CARS',
            },
        ),
    ]
