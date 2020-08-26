from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import userdata

def home(request):
    return render(request,'cryptonumjuggle/home.html')

@csrf_exempt
def setitem(request):
    if request.method == "POST":
        gameState = request.POST.get("gameState")
        wltaddr = request.POST.get("wltaddr")
        
        
        print(gameState,wltaddr)

        if(wltaddr != "0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            #save after checking if there is already a user with wlt addr
            if (wltuser.exists()):
                wltuser.update(gamestate=gameState)
            else:
                userdata.objects.create(wltaddr = wltaddr,gamestate=gameState)
                
            
    return HttpResponse("Saving some ")

#gets from sqlite
def getitem(request):
    if request.method == "GET":
        wltaddr = request.GET.get("wltaddr")

        if(wltaddr!="0"):
            wltuser = userdata.objects.filter(wltaddr = str(wltaddr))
            if(wltuser.exists()):
                gameState = wltuser[0].gamestate
                return HttpResponse(str(gameState))
            else:
                return HttpResponse("NoUser")
        
    return HttpResponse("get")
    
   