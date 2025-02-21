# Generated by Django 4.1 on 2024-09-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0039_alter_instagramapi_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(blank=True, max_length=500, null=True)),
                ('publishedAt', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('thumbnails', models.CharField(blank=True, max_length=100, null=True)),
                ('liveBroadcastContent', models.CharField(blank=True, max_length=100, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ministerios',
            name='logo_ministerio',
            field=models.ImageField(blank=True, help_text='Dimensão: 165 x 48 px', null=True, upload_to='ministerios/logo_ministerio'),
        ),
    ]
