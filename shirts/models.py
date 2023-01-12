from django.db import models

# Create your models here.
class Shirts(models.Model):
    maker = models.CharField(max_length=100)
    season = models.IntegerField()
    is_active = models.BooleanField(default=True)