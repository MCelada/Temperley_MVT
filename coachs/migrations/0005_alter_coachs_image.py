# Generated by Django 4.1.4 on 2023-01-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coachs', '0004_alter_coachs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachs',
            name='image',
            field=models.ImageField(blank=True, default='\\coachs_images\\silueta_tecnico.jpg', null=True, upload_to='coachs_images'),
        ),
    ]
