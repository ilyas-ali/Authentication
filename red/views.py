from django.shortcuts import render
from django.http import HttpResponse
from .models import People

def index(request):
        if request.method=="POST":
            fname1=request.POST.get('fname')
            lname1=request.POST.get('lname')
            email1=request.POST.get('email')
            num1=request.POST.get('num')
        
            pp=People(fname=fname1,lname=lname1,email=email1,num=num1)
            pp.save()
            

        return render(request,"red/index.html")

def fav(request):
    if request.method=="POST":
        email1=request.POST.get('email')
        people=People.objects.filter(email=email1).first()
        
        if people!=None:
            context={"fname":people.fname,"lname":people.lname,"email":people.email,"num":people.num}    
            return render(request,"red/yes.html",context)
            
        elif people==None:
            return render(request,"red/no.html")
    
    return render(request,"red/fav.html")