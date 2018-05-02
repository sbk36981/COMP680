# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm

# Create your models here.
class House(models.Model):
    house_name = models.CharField("House Name", max_length=200)
    request_date = models.DateTimeField("Date Published")
    csv_data = models.TextField("Raw CSV Data", blank=True)
    predicted_price = models.FloatField("Predicted Price", null=True, blank=True)
    actual_price = models.FloatField("Actual Price", null=True, blank=True)
    
    mssubclass_choices = [
        ("20","1-STORY 1946 & NEWER ALL STYLES"),
        ("30","1-STORY 1945 & OLDER"),
        ("40","1-STORY W/FINISHED ATTIC ALL AGES"),
        ("45","1-1/2 STORY - UNFINISHED ALL AGES"),
        ("50","1-1/2 STORY FINISHED ALL AGES"),
        ("60","2-STORY 1946 & NEWER"),
        ("70","2-STORY 1945 & OLDER"),
        ("75","2-1/2 STORY ALL AGES"),
        ("80","SPLIT OR MULTI-LEVEL"),
        ("85","SPLIT FOYER"),
        ("90","DUPLEX - ALL STYLES AND AGES"),
        ("120","1-STORY PUD (Planned Unit Development) - 1946 & NEWER"),
        ("150","1-1/2 STORY PUD - ALL AGES"),
        ("160","2-STORY PUD - 1946 & NEWER"),
        ("180","PUD - MULTILEVEL - INCL SPLIT LEV/FOYER"),
        ("190","2 FAMILY CONVERSION - ALL STYLES AND AGES")
    ]
    mssubclass = models.CharField("Dwelling Type", choices=mssubclass_choices, max_length=200, blank=False, default="1-STORY 1946 & NEWER ALL STYLES")

    lot_frontage = models.IntegerField("Lot Frontage", null=True, blank=True)
    lot_area = models.IntegerField("Lot Area", null=True, blank=True)
    overall_quality = models.IntegerField("Overall Quality", default=5, validators=[MaxValueValidator(10), MinValueValidator(1)], null=True, blank=True)
    overall_condition = models.IntegerField("Overall Condition", default=5, validators=[MaxValueValidator(10), MinValueValidator(1)],null=True, blank=True)
    year_built = models.IntegerField("Year Built", validators=[MaxValueValidator(9999), MinValueValidator(1)],null=True, blank=True)
    year_remodeled = models.IntegerField("Year Remodeled/Additions", validators=[MaxValueValidator(9999), MinValueValidator(1)],null=True, blank=True)
    
    masonry_veneer_choices = [
        ("BrkCmn","Brick Common"),
        ("BrkFace","Brick Face"),
        ("CBlock","Cinder Block"),
        ("None","None"),
        ("Stone","Stone")
    ]
    masonry_veneer = models.CharField("Masonry Veneer Type", choices=masonry_veneer_choices, max_length=200, default="None")
    bsmt_fin_sf1 = models.IntegerField("Basement Surface 1 Finish Sq Ft", null=True, blank=True)
    bsmt_fin_sf2 = models.IntegerField("Basement Surface 2 Finish Sq Ft", null=True, blank=True)
    bsmt_unf_sf = models.IntegerField("Basement Unfinished Sq Ft", null=True, blank=True)
    total_bsmt_sf = models.IntegerField("Basement Total Sq Ft", null=True, blank=True)
    first_floor_sf = models.IntegerField("First Floor Sq Ft", null=True, blank=True)
    second_floor_sf = models.IntegerField("Second Floor Sq Ft", null=True, blank=True)
    third_floor_sf = models.IntegerField("Third Floor Sq Ft", null=True, blank=True)
    fourth_floor_sf = models.IntegerField("Fourth Floor Sq Ft", null=True, blank=True)
    low_quality_finish_sf = models.IntegerField("Low Quality Finished Sq Ft (All Floors)", null=True, blank=True)
    above_ground_living_sf = models.IntegerField("Above Ground Living Area Sq Ft", null=True, blank=True)
    bsmt_full_bathrooms = models.IntegerField("# Basement Full Bathrooms", null=True, blank=True)
    bsmt_half_bathrooms = models.IntegerField("# Basement Half Bathrooms", null=True, blank=True)
    above_ground_full_bath = models.IntegerField("# Above Ground Full Bathrooms", null=True, blank=True)
    above_ground_half_bath = models.IntegerField("# Above Ground Half Bathrooms", null=True, blank=True)
    above_ground_full_bath = models.IntegerField("# Above Ground Full Bathrooms", null=True, blank=True)
    above_ground_bedrooms = models.IntegerField("# Above Ground Bedrooms", null=True, blank=True)
    above_ground_kitches = models.IntegerField("# Above Ground Kitchens", null=True, blank=True)
    above_ground_total_rooms = models.IntegerField("# Above Ground Total Rooms", null=True, blank=True)
    num_fireplaces = models.IntegerField("# Fireplaces", null=True, blank=True)

    garage_year_built = models.IntegerField("Garage Year Built", validators=[MaxValueValidator(9999), MinValueValidator(1)],null=True, blank=True)
    garage_cars = models.IntegerField("# Cars Garage",null=True, blank=True)
    garage_sf = models.IntegerField("Garage Sq Ft",null=True, blank=True)
    wood_deck_sf = models.IntegerField("Wood Deck Sq Ft",null=True, blank=True)
    open_porch_sf = models.IntegerField("Open Porch Sq Ft",null=True, blank=True)
    enclosed_porch_sf = models.IntegerField("Enclosed Porch Sq Ft",null=True, blank=True)
    three_season_porch_sf = models.IntegerField("3-Season Porch Sq Ft",null=True, blank=True)
    screen_porch_sf = models.IntegerField("Screen Porch Sq Ft",null=True, blank=True)
    pool_sf = models.IntegerField("Pool Sq Ft",null=True, blank=True)
    misc_value = models.FloatField("$ Value of Misc Features (2nd garage, elevator, tennis courts, etc)", null=True, blank=True)

    month_sold = models.IntegerField("Month Sold", validators=[MaxValueValidator(12), MinValueValidator(1)],null=True, blank=True)
    year_sold = models.IntegerField("Year Sold", validators=[MaxValueValidator(9999), MinValueValidator(1)],null=True, blank=True)

    sale_condition_choices = [
        ("Normal","Normal Sale"),
        ("Abnorml","Abnormal Sale -  trade, foreclosure, short sale"),
        ("AdjLand","Adjoining Land Purchase"),
        ("Alloca","Allocation - two linked properties with separate deeds, typically condo with a garage unit	"),
        ("Family","Sale between family members"),
        ("Partial","Home was not completed when last assessed (associated with New Homes)")
    ]
    sale_condition = models.CharField("Sale Condition", choices=sale_condition_choices, max_length=200, default="Normal")