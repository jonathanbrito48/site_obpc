# Generated by Django 4.1 on 2024-02-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0002_pastores_posicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministerios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ministerio', models.CharField(max_length=50)),
                ('descricao_ministerio', models.CharField(max_length=2000)),
                ('foto_ministerio', models.ImageField(upload_to='ministerios/foto_ministerios')),
                ('logo_ministerio', models.ImageField(upload_to='ministerios/logo_ministerio')),
            ],
        ),
        migrations.AlterField(
            model_name='pastores',
            name='biografia',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='pastores',
            name='foto',
            field=models.ImageField(upload_to='pastores/foto_pastor'),
        ),
    ]