from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import userdata

secret = "next lounge advance flat party turn hill fat exercise turn shiver penalty"

def home(request):
    return render(request,'cryptonumjuggle/home.html')

@csrf_exempt
def setitem(request):
    if request.method == "POST":
        gameState = request.POST.get("gameState")
        wltaddr = request.POST.get("wltaddr")
        
        
       # print(gameState,wltaddr)

        if(wltaddr != "0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            #save after checking if there is already a user with wlt addr
            if (wltuser.exists()):
                wltuser.update(gamestate=gameState)
            else:
                userdata.objects.create(wltaddr = wltaddr,gamestate=gameState)
            
    return HttpResponse("Saving some ")

@csrf_exempt
def fetchapi(request):
    if request.method == "POST":
        wltaddr = request.POST.get("wltaddr")
        if(wltaddr!=None):
            return HttpResponse(secret)
        else:
            return HttpResponse("Not logged in")
        
    return HttpResponse("fetchapi")


#gets from sqlite
def getitem(request):
    if request.method == "GET":
        wltaddr = request.GET.get("wltaddr")
       # print("wltaddre:"+str(wltaddr))
        if(wltaddr!="0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            if(wltuser.exists()):
                gameState = wltuser[0].gamestate
                return HttpResponse(str(gameState))
            else:
                return HttpResponse("NoUser")
        
    return HttpResponse("get")

def removeitem(request):
    if request.method == "GET":
        wltaddr = request.GET.get("wltaddr")
       # print("wltaddr:"+str(wltaddr))
        if(wltaddr!="0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            if(wltuser.exists()):
                wltuser.update(gamestate="")
                return HttpResponse("Cleared")
            else:
                return HttpResponse("NoUser")
        
    return HttpResponse("remove") 
   


@csrf_exempt
def setcnt(request):
    if request.method == "POST":
        counter = request.POST.get("counter")
        wltaddr = request.POST.get("wltaddr")
        
        
        print(counter,wltaddr)

        if(wltaddr != "0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            #save after checking if there is already a user with wlt addr
            if (wltuser.exists()):
                wltuser.update(counter=counter)
            else:
                userdata.objects.create(wltaddr = wltaddr,counter=counter)
            
    return HttpResponse("Saving counter ")

def getcnt(request):
    if request.method == "GET":
        wltaddr = request.GET.get("wltaddr")
       # print("wltaddre:"+str(wltaddr))
        if(wltaddr!="0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            if(wltuser.exists()):
                counter = wltuser[0].counter
                return HttpResponse(str(counter))
            else:
                return HttpResponse("NoUser")
        
    return HttpResponse("get")