from turtle import ht
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def say_hello(request):
    #now=datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    person={'name':'admin'}
    return render(request,'hello.html',context=person)

def homepage(request):
    return render(request,'home.html')
