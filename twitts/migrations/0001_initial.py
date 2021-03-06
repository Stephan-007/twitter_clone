# Generated by Django 3.2.9 on 2021-11-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Add a name', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='body')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Created time')),
            ],
            options={
                'db_table': 'twitt',
            },
        ),
    ]
