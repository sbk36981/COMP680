# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import requests, json
from django.conf import settings

# Create your views here.

from .models import House

@login_required
def index(request):
    house_list = House.objects.order_by('-request_date')
    context = {'latest_houses_list' : house_list}
    return render(request, 'houses/index.html', context)

@login_required
def housedetail(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    return render(request, "houses/detail.html", {'house' : house})

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
        house.predicted_price = json.loads(r.content)["predictions"][0]["score"]
    except KeyError:
        return HttpResponseRedirect(reverse('cusportal:housedetail', args=[house.id]))
    house.save()
    return HttpResponseRedirect(reverse('cusportal:housedetail', args=[house.id]))
