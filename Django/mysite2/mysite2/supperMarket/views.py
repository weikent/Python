from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from mysite2.supperMarket.models import MainSort, SubSort, ImagePath



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


# Create your views here.
