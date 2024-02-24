from django.db import models

# Create your models here.

class Customer(models.Model):
    c_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length = 90)
    lname = models.CharField(max_length = 90)
    product = models.CharField(max_length = 90)
    qty = models.IntegerField()
    price = models.FloatField()
