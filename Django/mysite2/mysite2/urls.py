from django.conf.urls import patterns, include, url
from mysite2.views import hello
from mysite2.views import current_datetime
from mysite2.views import hours_ahead
from mysite2.views import test_method_call
from mysite2.views import book_list
from mysite2.views import display_meta
from mysite2.views import two_offset
from mysite2.contact.views import contact

# from books.views import search_form
from mysite2.books import views
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^mysite2/', include('mysite2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', hello),
    url(r'^$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time/plus/p1(\d{1,2})p2(\d{1,3})/$', two_offset),
    url(r'^test/person/$', test_method_call),
    url(r'^test/book_list/$', book_list),
    url(r'^meta/$', display_meta),
    # url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
)
