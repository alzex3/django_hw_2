from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        lst = [i for i in reader]

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(lst, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
