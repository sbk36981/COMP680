# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
    house_name = models.CharField(max_length=200)
    request_date = models.DateTimeField('date published')
    csv_data = models.TextField()
    predicted_price = models.DecimalField(max_digits=20, decimal_places=20)
    actual_price = models.DecimalField(max_digits=20, decimal_places=20)
