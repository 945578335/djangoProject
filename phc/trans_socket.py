import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from phc import models

def trans_page(request):
    return render(request, 'trans_page.html')