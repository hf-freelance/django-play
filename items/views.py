from django.shortcuts import render
from django.http import HttpResponse

from items.models import Item, Category

# Create your views here.


def getAllItems(request):
    items = Item.objects.all()
    return HttpResponse(items)

def getAllCategories():
    Categories = Category.objects.all()
    return HttpResponse(Categories)


def findOneItem(request):
    try:
        id = request.GET["id"]
        item = Item.objects.get(id=id)
    except Item.DoesNotExist as e:
        return HttpResponse(status=404)
    return HttpResponse(item)

"""
def addOneItem(request):
    id = request.GET["id"]
    return HttpResponse(Item.objects.get(id=id))

def updateAvailability(request):
    id = request.GET["id"]
    return HttpResponse(Item.objects.get(id=id))    
"""