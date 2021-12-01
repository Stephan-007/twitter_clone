# Generated by Django 3.2.9 on 2021-11-28 15:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitts', '0004_twitt_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitt',
            name='pic',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]