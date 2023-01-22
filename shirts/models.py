from django.db import models

# Create your models here.
class Shirts(models.Model):
    maker = models.CharField(max_length=100)
    season = models.IntegerField()
    image = models.ImageField(upload_to='shirts_images',null=True, blank = True)
    is_active = models.BooleanField(default=True)