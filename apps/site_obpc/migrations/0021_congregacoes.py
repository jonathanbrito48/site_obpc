# Generated by Django 4.1 on 2024-03-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0020_ministerios_facebook_ministerios_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congregacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_congregacao', models.CharField(max_length=100)),
                ('descricao_congregacao', models.CharField(blank=True, max_length=2000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('endereco', models.CharField(blank=True, max_length=300, null=True)),
                ('link_maps', models.CharField(blank=True, max_length=700, null=True)),
                ('cultos', models.CharField(blank=True, max_length=300, null=True)),
                ('foto_banner', models.ImageField(upload_to='congregacoes/banner')),
                ('foto_dirigentes', models.ImageField(upload_to='congregacoes/digirentes')),
            ],
        ),
    ]