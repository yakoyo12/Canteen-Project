from django.db import models

class Canteen(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
