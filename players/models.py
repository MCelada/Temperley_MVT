from django.db import models

# Create your models here.
class Players(models.Model):
    CONDITION_CHOICES = (
        ('arquero', 'arquero'),
        ('defensor', 'defensor'),
        ('volante', 'volante'),
        ('delantero', 'delantero'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.FloatField()
    position = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)