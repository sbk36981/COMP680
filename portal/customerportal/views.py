# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import requests, json, datetime
from django.conf import settings
from math import exp

# Create your views here.

from .models import House
from .forms import HouseForm

@login_required
def index(request):
    house_list = House.objects.order_by('-request_date')
    context = {'latest_houses_list' : house_list}
    return render(request, 'houses/index.html', context)

@login_required
def housedetail(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    form = HouseForm(instance=house)
    return render(request, "houses/detail.html", {'form' : form})

@login_required
def prediction(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    body = {'datain' : house.csv_data}
    payload = json.dumps(body)
    endpoint = 'https://e2g8b7xnl6.execute-api.us-west-2.amazonaws.com/development/SingleHousingPrediction'
    headers = {
        'Content-Type' : 'application/json',
        'x-api-key' : settings.X_AMAZON_API_KEY
    }
    r = requests.post(endpoint, headers=headers, data=payload)
    try:
        house.predicted_price = exp(json.loads(r.content)["predictions"][0]["score"])
    except KeyError:
        return HttpResponseRedirect(reverse('cusportal:housedetail', args=[house.id]))
    house.save()
    return HttpResponseRedirect(reverse('cusportal:housedetail', args=[house.id]))

@login_required
def add_house(request):
    if request.method  == 'POST':
        form = HouseForm(request.POST)
        form.request_date = datetime.date.today()

        # Check if form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cusportal:index'))
    else:
        form = HouseForm()
    return render(request, "houses/add.html", {"form": form})