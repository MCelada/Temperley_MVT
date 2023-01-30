from django.db import models

# Create your models here.
class Shirts(models.Model):
    maker = models.CharField(max_length=100)
    season = models.IntegerField()
    image = models.ImageField(verbose_name = 'shirt_image', upload_to='shirts_images',null=True, blank = True,  default='\shirts_images\silueta_camiseta.jpg')
    is_active = models.BooleanField(default=True)
