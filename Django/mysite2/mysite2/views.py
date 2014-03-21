from django.http import HttpResponse
# from django.template import Template
# from django.template import Context
# from django.template.loader import get_template
# from mysite2 import settings
from django.shortcuts import render_to_response



from django.shortcuts import render_to_response
import MySQLdb

from  mysite2.supperMarket import views


def book_list(request):
    db = MySQLdb.connect(user='root', db='mydb', passwd='wsj673756', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})


def hello(request):
    """
    
    Arguments:
    - `request`:
    """
    return HttpResponse("Hello World");


import datetime

def current_datetime(request):
    """
    
    Arguments:
    - `request`:
    """
    current_time = datetime.datetime.now()

    # t = get_template("current_time.html")
    # # html = t.render(Context({"current_time" : now}))
    # html = t.render(Context(locals()))
    # # html = "<html><body>This time is %s. </body></html> " % now
    # # html1 = settings.TEMPLATE_DIRS
    mainSort = views.mainSort()
    imagePath = views.imagePath()
    index = []

    mainPageSort1= []
    mainPageSort2 = []
    mainPageSort3 = []

    for item in imagePath:
        if item.name == 'index':
            index = item
        if item.name == 'cereal&oil':
            mainPageSort1 = item
        if item.name == 'seasonings':
            mainPageSort2 = item
        if item.name == 'snack':
            mainPageSort3 = item


    return render_to_response("superMarket/main.html", {"current_time": current_time, 'title':'current_time', 'mainSort': mainSort, 'index': index, 'mainPageSort1' : mainPageSort1, 'mainPageSort2' : mainPageSort2, 'mainPageSort3' : mainPageSort3})


def subSort(request):
    """
    
    Arguments:
    - `request`:
    """

    mainSortItems = views.mainSort()
    subSortItems = views.subSort()

    mainSortItem = mainSortItems[0]
    brand = views.brand()
    kind = views.kind()

    item = []

    if 'sort' in request.GET:
        sort = request.GET['sort']
        if not sort:
            return render_to_response("404.html")
        else:
            item = views.item(100)
            return render_to_response("superMarket/subSort.html", {'title' : 'subSort', 'items' : item, 'mainSortItems' : mainSortItems, 'subSortItems' : subSortItems, 'mainSortItem' : mainSortItem})

    return render_to_response("superMarket/subSort.html", {'title' : 'subSort', 'items' : item})

from django.http import Http404
def hours_ahead(request, offset):
    """
    
    Arguments:
    - `request`:
    - `offest`:
    """
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)



def two_offset(request, offset1, offset2):
    """
    
    Arguments:
    - `request`:
    - `offset1`:
    - `offset2`:
    """
    try:
        offset1 = int(offset1)
        offset2 = int(offset2)
    except ValueError:
        raise Http404()

    html = "<html><body>first offset is %s, second offset is %s</body></html>" % (offset1, offset2)
    return HttpResponse(html)

class SilentAssertionError(AssertionError):
    silent_variable_failure = True

class personClass(object):
    """
    """
    
    def __init__(self):
        """
        """
    def first_name(self):
        """
        
        Arguments:
        - `self`:
        """
        #raise AssertionError, "foo"
        raise SilentAssertionError, 'a'
        return 'aa'

        
        


from django.template import Template, Context
def test_method_call(request):
    """
    
    Arguments:
    - `request`:
    """
    p = personClass()
    t = Template("My name is {{ person.first_name }}.")
    c = Context({'person':p})
    html = t.render(c)
    return HttpResponse(html)



def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
