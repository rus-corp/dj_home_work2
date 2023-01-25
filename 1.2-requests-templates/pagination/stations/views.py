from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pprint import pprint



def index(request):
    return redirect(reverse('bus_stations'))


bus_stat = []
with open("data-398-2018-08-30.csv", newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        bus_stat.append(row)

        



def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stat, 10)
    page = paginator.get_page(page_number) 
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
