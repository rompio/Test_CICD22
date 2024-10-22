from django.shortcuts import render
from shop.models import Item
from django.http import HttpResponse

def index(request):
    items = Item.objects.all()
    return HttpResponse(items)