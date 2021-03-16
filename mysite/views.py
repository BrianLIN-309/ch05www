from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def homepage(request):
    return HttpResponse("Hello World!")

def homepage(request, testmode):
    html = "<h2>Hello, testmode is {}</h2><hr>".format(testmode)
    return HttpResponse(html)

def about(request,author_no=0):
    html = "<h2>Here is Author{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)


def listing(request, yr, mon, day):
    html = "<h2>List Date is {}/{}/{}</h2><hr>".format(yr, mon, day)
    return HttpResponse(html)

def post(request, yr, mon, day, post_num):
    html = "<h2>{}/{}/{}:Post Number:{}</h2><hr>".format(yr, mon, day, post_num)
    return HttpResponse(html)

def post01(request, yr, mon, day, post_num):
    html = "<a href='{}'>Show the Post</a>".format(reverse('post-url', args=(yr, mon, day, post_num,)))
    return HttpResponse(html)
# Create your views here.
