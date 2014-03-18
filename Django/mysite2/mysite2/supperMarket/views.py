# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from mysite2.supperMarket.models import MainSort, SubSort, ImagePath, Brand, Kind, Item



def mainSort():
    """
    
    Arguments:
    - `self`:
    """
    mainSort = MainSort.objects.all()
    return mainSort




def imagePath():
    """
    
    Arguments:
    - `self`:
    """
    imagePath = ImagePath.objects.all()
    return imagePath


def brand():
    """
    """
    brand = Brand.objects.all()
    return brand

def kind():
    """
    """
    kind = Kind.objects.all()
    return kind

def item(sort):
    """
    """
    if sort == 100:
        item = Item.objects.filter(sort_id = 1) # 1 = 进口食品

    return item



# Create your views here.
