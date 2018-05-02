# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
from .models import House

class HouseResource(resources.ModelResource):
    class Meta:
        model = House
        
@admin.register(House)
class HouseAdmin(ImportExportModelAdmin):
    resource_class = HouseResource


