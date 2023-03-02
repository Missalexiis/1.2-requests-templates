from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def bus_stations(request):
    paginator = Paginator(data, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    prev_page = paginator.get_page(page_number-1)
    next_page = paginator.get_page(page_number+1)

    context = {
        'bus_stations': data,
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page,
    }
    return render(request, 'stations/index.html', context)