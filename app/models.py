from django.db import models

# Create your models here.

class ProductOrder(models.Model):
    supplier = models.CharField(max_length = 100)
    po_number = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    properties = models.TextField()
    
class Docket(models.Model):
    name = models.CharField(max_length =50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    hours = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    supplier  = models.CharField(max_length=50)
    po_number = models.CharField(max_length= 50)
    description = models.TextField(blank=True)