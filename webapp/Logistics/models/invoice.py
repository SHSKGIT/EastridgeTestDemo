from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class Invoice(models.Model):

    date = models.DateField(unique=True)


class InvoiceItem(models.Model):

    units = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

