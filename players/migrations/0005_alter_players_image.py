# Generated by Django 4.1.4 on 2023-02-04 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_alter_players_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='players_images', verbose_name='imagen'),
        ),
    ]