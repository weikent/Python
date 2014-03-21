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
    mainSort = MainSort.objects.filter(id__lte = 15)  # "id__lte = 15 " 等于 "where id <= 15"
    return mainSort


def subSort():
    """
    """
    subSort = SubSort.objects.all()
    return subSort


def imagePath():
    """
    
    Arguments:
    - `self`:
    """
    imagePath = ImagePath.objects.order_by('id').all()
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
