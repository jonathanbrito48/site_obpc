# Generated by Django 4.1 on 2024-09-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0037_instagramapi_permalink'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramapi',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
