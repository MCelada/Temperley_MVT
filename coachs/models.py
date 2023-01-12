from django.db import models

# Create your models here.
class Coachs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    period = models.IntegerField()
    is_active = models.BooleanField(default=True)

    