# Generated by Django 4.1 on 2024-02-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_obpc', '0012_alter_ministerios_card_ministerio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministerios',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
