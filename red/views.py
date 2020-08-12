from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
        if request.method=="POST":
            user1=request.POST.get('user')
            pass1=request.POST.get('pass')
            pass2=request.POST.get('pass1')
            fname1=request.POST.get('fname')
            lname1=request.POST.get('lname')
            email1=request.POST.get('email')
            num1=request.POST.get('num')
            
            
            if pass1==pass2:
                
                if User.objects.filter(username=user1).exists():
                    error_messages={"message1":"User already exists"}
                    return render(request,"red/index.html",context=error_messages)
            
                else:
                    user=User.objects.create_user(username=user1,email=email1,password=pass1,first_name=fname1,last_name=lname1)
                    user.save()
                    profile=Profile()
                    profile.user=user
                    profile.num=num1
                    profile.save()
                    login(request,user)
                    context={"user1":user1}
                    return render(request,"red/yes.html",context)
                    
            
            else:
                error_messages={"message1":"Passwords do not match"}
                return render(request,"red/index.html",context=error_messages)
                
            
            

        return render(request,"red/index.html")

def fav(request):
    if request.method=="POST":
        user1=request.POST.get('user')
        pass1=request.POST.get('pass')
        user=authenticate(username=user1,password=pass1)
        if user is not None:
            if user.is_active:
                login(request,user)
                context={"user1":user1}
                return render(request,"red/no.html",context)
            
        
        else:
            error_messages={"message1":"Invalid credentials"}
            return render(request,"red/fav.html",context=error_messages)
    
    return render(request,"red/fav.html")

def log(request):
    logout(request)
    return render(request,"red/out.html")