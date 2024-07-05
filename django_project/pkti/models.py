from django.db import models


# Create your models here.

class Sensor(models.Model):
    sensor_id = models.IntegerField()
    degree = models.FloatField()
    reika = models.FloatField()
    rate = models.FloatField()
    charge = models.FloatField()
    signal = models.FloatField()
    reading_date = models.DateTimeField(auto_now_add=True)


