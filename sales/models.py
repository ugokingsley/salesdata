from django.db import models

# Create your models here.


class SalesData(models.Model):
    invoice = models.CharField(max_length=200)
    stockcode = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    invoicedate = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    customerid = models.IntegerField()

    def __str__(self):
        return self.description