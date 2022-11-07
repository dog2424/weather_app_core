from django.db import models


class Weather(models.Model):
    id = models.BigAutoField(primary_key=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    description = models.TextField(max_length=4000, null=True)
    temp = models.CharField(max_length=128)
