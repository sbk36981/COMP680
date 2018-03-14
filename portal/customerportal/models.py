# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
    house_name = models.CharField(max_length=200)
    request_date = models.DateTimeField('date published')
    csv_data = models.TextField(blank=True)
    predicted_price = models.FloatField(null=True, blank=True)
    actual_price = models.FloatField(null=True, blank=True)
