# Generated by Django 4.1 on 2024-09-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0035_instagramtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagramapi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('media_type', models.CharField(blank=True, max_length=500, null=True)),
                ('caption', models.CharField(blank=True, max_length=5000, null=True)),
                ('media_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=100, null=True)),
                ('children', models.CharField(blank=True, max_length=1000, null=True)),
                ('thumbnail_url', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]