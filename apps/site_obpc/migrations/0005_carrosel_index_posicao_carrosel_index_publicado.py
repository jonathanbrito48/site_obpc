# Generated by Django 4.1 on 2024-02-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0004_carrosel_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrosel_index',
            name='posicao',
            field=models.IntegerField(default=None, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='carrosel_index',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
