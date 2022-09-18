from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Parientes(models.Model):
    nombreyapellido = models.CharField(max_length=50)
    fechanacimiento = models.DateField()
    edad = models.IntegerField()
