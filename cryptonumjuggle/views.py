from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'cryptonumjuggle/home.html')

def setitem(request):
    return HttpResponse("some value")
#gets from sqlite
def getitem(request):
    val = 0
    return HttpResponse(val)