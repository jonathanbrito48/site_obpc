# Generated by Django 4.1 on 2024-09-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0038_instagramapi_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramapi',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
