from django.http import HttpResponse
# from django.template import Template
# from django.template import Context
# from django.template.loader import get_template
# from mysite2 import settings
from django.shortcuts import render_to_response



from django.shortcuts import render_to_response
import MySQLdb

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
    return render_to_response("current_time/current_time.html", {"current_time": current_time})

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
