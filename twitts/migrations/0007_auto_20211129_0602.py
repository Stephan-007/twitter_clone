# Generated by Django 3.2.9 on 2021-11-29 06:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitts', '0006_rename_pic_twitt_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitt',
            name='likes',
            field=models.PositiveBigIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='twitt',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
