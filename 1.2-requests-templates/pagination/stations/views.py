import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

with open ('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    my_csvfile = csv.DictReader (csvfile,delimiter = ",")
    
print(my_csvfile)

def index(request):
    return redirect(reverse('bus_stations'))

with open ('Z:\\2021-09-23_PYTHON\django\dj-home-jobs\dj-homeworks\\1.2-requests-templates\pagination\data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    my_csvfile = csv.DictReader (csvfile,delimiter = ",")
    print(my_csvfile)
    y = []
    for x in my_csvfile:
      y.append({'Name':x['Name'], 'Street': x['Street'], 'District':x['District']})  
    #   print (y)
    #   break

def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    
    paginator = Paginator (y,5)
    page = paginator.get_page(page_number)
    context = {
              'page': page,
              }
    return render(request, 'stations/index.html', context)
