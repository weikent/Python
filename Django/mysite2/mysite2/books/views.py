# Create your views here.

from django.shortcuts import render_to_response

def search_form(request):
    """
    
    Arguments:
    - `request`:
    """
    return render_to_response('search_form.html')


from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite2.books.models import Book

# def search(request):
#     """
    
#     Arguments:
#     - `request`:
#     """
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
    
#     if 'q1' in request.GET:
#         message1 = 'You second parameter is : %r' % request.GET['q1']
#     else:
#         message1 = 'You second parameter is empty'
#     return HttpResponse(message + '\r\n' + message1)

# def search(request):
#     """
    
#     Arguments:
#     - `request`:
#     """
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.objects.filter(title__icontains=q)
#         return render_to_response('search_results.html', {'books': books, 'query' : q})
#     else:
#         return render_to_response('search_form.html', {'error': True})
#         # return HttpResponse('Please submit a search term.')


def search(request):
    """
    
    Arguments:
    - `request`:
    """
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books' : books, 'query':q})
    
    return render_to_response('search_form.html', {'error':error})
