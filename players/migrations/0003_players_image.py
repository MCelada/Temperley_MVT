# Generated by Django 4.1.4 on 2023-01-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_players_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='players_images'),
        ),
    ]
