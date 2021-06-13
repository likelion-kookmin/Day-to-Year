from django.db import models

# Create your models here.
class Rental(models.Model): 
    product = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    price = models.IntegerField()
    location_city = models.CharField(max_length=10)
    location_detail = models.CharField(max_length=10)
    rentterm = models.IntegerField()
    information = models.CharField(max_length=300)
    
    def __str__(self):
        return self.product
